---
name: lan-device-recon
description: "LAN device enum and router recon from Windows."
---

# LAN Device Recon (Windows Host)

Session-tested workflow for local network device enumeration and router attack-surface mapping from Windows.

## Workflow

### Step 1: WiFi AP Discovery

```bash
netsh wlan show networks mode=bssid
```

Extract: SSID, signal %, radio type, channel, **connected stations count**, channel utilization %.

### Step 2: LAN Subnet & ARP Discovery

```bash
ipconfig | grep -A 5 "WLAN"
arp -a
netsh interface ip show neighbors "WLAN"
```

**GBK pitfall**: `netsh`/`arp` output is GBK on Chinese Windows. Pipe through `2>&1 | cat` or use Python `decode('gbk', errors='replace')`.

### Step 3: Ping Sweep (80-thread Python)

```python
import subprocess, concurrent.futures

def ping(ip):
    try:
        r = subprocess.run(['ping', '-n', '1', '-w', '300', ip],
                           capture_output=True, timeout=2)
        out = r.stdout.decode('gbk', errors='replace')
        if 'TTL=' in out:
            for line in out.split('\n'):
                if 'TTL=' in line:
                    return (ip, line.strip())
    except: pass
    return None

with concurrent.futures.ThreadPoolExecutor(max_workers=80) as ex:
    futs = {ex.submit(ping, f'192.168.3.{i}'): i for i in range(1, 255)}
    for f in concurrent.futures.as_completed(futs):
        r = f.result()
        if r: print(r)
```

**Pitfall**: Never use `text=True` in subprocess on Windows — it translates `\n` to `\r\n` and breaks downstream parsing. Always raw bytes + explicit decode.

### Step 4: TTL OS Fingerprinting

| TTL | OS |
|-----|-----|
| 128 | Windows |
| 64 | Linux / embedded / router |
| 255 | Network equipment |
| 62-63 | Linux behind 1-2 hops |

### Step 5: MAC OUI Lookup

```python
import urllib.request
req = urllib.request.Request(
    f'https://api.macvendors.com/{mac}',
    headers={'User-Agent': 'Mozilla/5.0'})
vendor = urllib.request.urlopen(req, timeout=5).read().decode()
```

**MAC randomization**: First byte bit 1 set (e.g. `02:`, `22:`, `3E:`, `EE:`) = locally-administered (randomized) MAC. OUI lookup returns 404. Common on modern phones with privacy MAC.

### Step 6: Multi-Subnet Sweep

Chinese apartment/hotel networks often have multiple /24 subnets. Always sweep adjacent subnets (192.168.0-5.0/24) when gateway routes cross-subnet pings. TTL > 60 on cross-subnet hosts confirms routing (not direct L2).

### Step 7: Router Fingerprinting via Frontend JS

```bash
curl -sk https://<gateway>/ | grep -i "script.*src"
curl -sk https://<gateway>/js/module_list.js
```

## NETCORE (磊科) CS-TW3 Pattern

Identified by `vendor:"NETCORE"`, `module:"CS-TW3"` in module_list.js.

### ubus JSON-RPC API

OpenWrt-based with `/ubus` endpoint. Login flow:

1. `routerd.get_rand_key` returns 64-char hex `rand_key`
2. Split: `key_index = rand_key[:32]`, `key = rand_key[32:64]`
3. AES-128-CBC encrypt password: key=hex portion, IV=`poiewjhw49q35j4n` (hardcoded!)
4. Encrypted password = `key_index + hex(ciphertext)`
5. `routerd.login` returns `ubus_rpc_session` token

### Authenticated ubus Calls

```python
def ubus_call(token, obj, method, params=None):
    data = json.dumps({
        'jsonrpc': '2.0', 'method': 'call',
        'params': [token, obj, method, params or {}], 'id': 1
    })
    # POST to https://<router>/ubus
```

Key methods: `devices_app.get_host_info`, `routerd.router_info`, `routerd.wificfg_get`, `routerd.dhcp_leases`

### Lockout Behavior

Wrong passwords trigger ErrCode `-11002` with Timeout countdown (~60s). Must wait before retrying.

### Default Credentials

Username: `useradmin`. Common passwords: admin, password, 12345678, 1234567890, 123456, 00000000, 88888888.

## Pitfalls

- **execute_code + terminal encoding**: Write scan scripts to files first, then `terminal(f'python "{path}"')` to avoid nested quote escaping
- **browser_navigate fails on self-signed certs**: Use `curl -sk` or Python `ssl.CERT_NONE` instead of browser for HTTPS router panels
- **ARP cache is lazy**: Must ping targets first to populate ARP; `netsh interface ip show neighbors` only shows cached entries
- **WiFi AP device count != your subnet**: AP reports total across all VLANs/subnets; your ping sweep only sees your L2 segment
