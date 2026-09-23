"""
Windows LAN device scanner — ping sweep + ARP + OUI lookup.
Usage: python win_lan_scan.py [subnet]
  subnet: CIDR notation, default 192.168.3.0/24
"""
import subprocess, concurrent.futures, sys, json, urllib.request

def ping(ip):
    try:
        r = subprocess.run(['ping', '-n', '1', '-w', '300', ip],
                           capture_output=True, timeout=2)
        out = r.stdout.decode('gbk', errors='replace')
        if 'TTL=' in out:
            ttl = None
            time_ms = None
            for line in out.split('\n'):
                if 'TTL=' in line:
                    for part in line.split():
                        if 'TTL=' in part:
                            ttl = part.split('=')[1]
                        if '时间=' in part or 'time=' in part:
                            time_ms = part.split('=')[1].rstrip('ms').strip('<')
                    return {'ip': ip, 'ttl': ttl, 'time_ms': time_ms}
    except:
        pass
    return None

def oui_lookup(mac):
    try:
        req = urllib.request.Request(
            f'https://api.macvendors.com/{mac}',
            headers={'User-Agent': 'Mozilla/5.0'})
        return urllib.request.urlopen(req, timeout=5).read().decode()
    except:
        return 'Unknown'

def get_arp():
    """Parse arp -a output into {ip: mac} dict."""
    r = subprocess.run(['arp', '-a'], capture_output=True, text=False)
    out = r.stdout.decode('gbk', errors='replace')
    entries = {}
    for line in out.split('\n'):
        parts = line.split()
        if len(parts) >= 2 and '.' in parts[0]:
            ip = parts[0]
            mac = parts[1].replace('-', ':')
            if mac != '00:00:00:00:00:00' and not mac.startswith('ff:ff'):
                entries[ip] = mac
    return entries

def main():
    import ipaddress
    subnet = sys.argv[1] if len(sys.argv) > 1 else '192.168.3.0/24'
    net = ipaddress.ip_network(subnet, strict=False)
    hosts = [str(h) for h in net.hosts()]

    print(f"Scanning {subnet} ({len(hosts)} hosts)...\n")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=80) as ex:
        futs = {ex.submit(ping, h): h for h in hosts}
        for f in concurrent.futures.as_completed(futs):
            r = f.result()
            if r:
                results.append(r)

    results.sort(key=lambda x: [int(p) for p in x['ip'].split('.')])

    # Get ARP cache for MAC addresses
    arp = get_arp()

    print(f"{'IP':<18} {'TTL':>4} {'Time':>6} {'MAC':<18} {'Vendor'}")
    print("-" * 80)
    for r in results:
        mac = arp.get(r['ip'], '-')
        vendor = oui_lookup(mac) if mac != '-' else '-'
        print(f"{r['ip']:<18} {r['ttl']:>4} {r['time_ms']:>5}ms {mac:<18} {vendor}")

    print(f"\nTotal alive: {len(results)}")

if __name__ == '__main__':
    main()
