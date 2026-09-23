---
name: security-agent-framework
description: "构建 AI 驱动自动化渗透 Agent 框架。覆盖架构/双模式/工具注册/Docker Kali/Web 仪表盘。"
tags: [security-agent, automation, docker, kali, pentest-framework]
---

# Security Agent Framework 构建指南

构建 AI 驱动的自动化渗透测试 Agent 框架的完整方法论。

## 架构模式

```
┌─────────────────────────────────────────────┐
│              编排器 (Orchestrator)             │
│  5阶段状态机: RECON→SCAN→EXPLOIT→POST→REPORT  │
├──────────┬──────────┬──────────┬─────────────┤
│ 侦察Agent│ 扫描Agent│ 利用Agent │ 报告Agent    │
├──────────┴──────────┴──────────┴─────────────┤
│           工具注册中心 (100+ 工具)              │
├──────────────────┬───────────────────────────┤
│   知识图谱 (Kg)   │    Docker Kali 沙箱       │
├──────────────────┴───────────────────────────┤
│  4 Provider: OpenAI / Anthropic / Kimi / Ollama│
└─────────────────────────────────────────────┘
```

## 核心模块

### 1. 编排器 (Orchestrator)
- 状态机驱动 5 阶段攻击链
- 每阶段: Agent.plan() → execute → Agent.reflect()
- 反思机制: LLM 判断是否需要回退/继续
- 预算控制: max_tool_calls + max_llm_tokens

### 2. 专业 Agent
| Agent | 职责 | LLM 依赖 |
|-------|------|---------|
| ReconAgent | 子域枚举/端口扫描/指纹识别 | ✅ 规划 |
| ScannerAgent | 漏洞扫描/弱点检测 | ✅ 规划 |
| ExploiterAgent | 漏洞利用/PoC验证 | ✅ 规划 |
| PostExploitAgent | 提权/横向/数据收集 | ✅ 规划 |
| ReporterAgent | 报告生成/修复建议 | ✅ 生成 |

### 3. 工具注册中心
```python
registry.register(ToolDef(
    name="nmap_scan",
    description="Nmap 全端口扫描",
    category="recon",
    phase="recon",
    mitre_technique="T1046",
    command_template="nmap -sV -sC -p- {target}",
    parameters={"type":"object","properties":{"target":{"type":"string"}},"required":["target"]},
    timeout_s=600,
    requires_sandbox=True,
))
```

### 4. 双模式运行
- **LLM 模式**: 有 API key 时，Agent 自主规划工具调用
- **规则引擎模式**: 无 API key 时，硬编码攻击模板全自动
- 检测逻辑: `has_api_key = bool(config.llm.api_key)`

### 5. 工具可用性检测
```python
import shutil
_TOOL_CACHE = {}
def _check_tool(name):
    if name in _TOOL_CACHE: return _TOOL_CACHE[name]
    binary = bin_map.get(name, name)  # 工具名→二进制名映射
    found = shutil.which(binary) is not None
    _TOOL_CACHE[name] = found
    return found
```
- 前端根据 `/api/tools-status` 显示可用/未安装 badge
- 未安装工具显示安装命令

### 6. Docker Kali 部署
```dockerfile
FROM kalilinux/kali-rolling
# 国内镜像源
RUN echo "deb https://mirrors.aliyun.com/kali kali-rolling main non-free contrib" > /etc/apt/sources.list
# 安装工具
RUN apt-get update && apt-get install -y nmap nikto hydra whatweb ...
RUN pip3 install sqlmap nuclei httpx impacket
# Go 工具
RUN wget ffuf binary...
WORKDIR /opt/hexagent
COPY . /opt/hexagent
EXPOSE 8080
CMD ["python3", "-c", "from hexagent.web.routes import start_web; start_web(8080)"]
```

## 完整工具库 (100+)

| 分类 | 数量 | 代表工具 |
|------|------|---------|
| 侦察 | 14 | nmap×3, masscan, subfinder, amass, theharvester, whatweb, httpx |
| Web | 12 | nikto, ffuf×3, gobuster, nuclei, wpscan, testssl |
| 注入 | 11 | sqlmap×2, xsstrike, dalfox, cmdi, lfi, ssrf, xxe |
| 破解 | 8 | hydra×5, medusa, john, hashcat |
| 内网 | 8 | bloodhound, kerberoast, secretsdump, cme, enum4linux |
| 提权 | 9 | linpeas, winpeas, seatbelt, rubeus, mimikatz |
| 隧道 | 7 | chisel, ligolo, ssh, proxychains, socat, frp |
| 云 | 5 | cloud_enum, pacu, s3, metadata, scoutsuite |
| MITM | 4 | responder, bettercap, mitmproxy, arpspoof |
| 泄露 | 5 | github_dork, git, env, backup, pastebin |
| 中国工具 | 7 | 蚁剑, 冰蝎×2, 哥斯拉, 御剑, 天蝎, cobra |
| 社工 | 2 | setoolkit, king-phisher |
| 无线 | 2 | aircrack-ng, wifite |

## Web 仪表盘设计

- 三页面: 仪表盘(实时数据) / 武器库(工具卡片) / 终端
- 全中文界面，苹果极简风格
- 工具卡片点击→弹窗填参数→执行
- 工具可用性检测: 绿=可用 / 红=未安装

## Pitfalls

- **Docker 国内网络**: Kali 官方源不通，必须换阿里云镜像 (`mirrors.aliyun.com/kali`)；SSL 证书问题需先装 `ca-certificates`；pip 用阿里云 PyPI 镜像
- **工具名映射**: `subfinder` 的 apt 包名 ≠ 二进制名，需 bin_map 映射
- **Flask threaded=True**: 必须开，否则扫描阻塞轮询
- **Python f-string 嵌套引号**: `<3.12` 不支持，先赋临时变量
- **三引号 HTML**: `r"""..."""` 中不能出现 `"""`，否则提前终结
- **pip install -e . WinError 32**: 上一个 exe 还在跑 → `taskkill /F /IM xxx.exe`
- **subprocess text=True 中文乱码**: `PYTHONUTF8=1` + 脚本文件

## 纯 Go 极致版（Kur1sulab-soul go-soul）

把 Python/Flask 版重写成纯 Go（net/http + goroutine）后，API 响应 <10ms、工具请求 ~7ms，比 Flask 快 10x。8.4MB 单 exe。工程上踩的坑（都会悄悄吞时间）：

### Go 环境
- Windows 无 Go：竟无 winget/choco → 走代理 `curl -L -o go.zip https://mirrors.aliyun.com/golang/go1.24.1.windows-amd64.zip`（阿里云镜像通，go.dev 也通走 Clash）解压到 `C:\Go`
- bash 里设 Go 环境变量必须 Windows 反斜杠绝对路径：`export GOROOT="C:\\Go\\go"`（`/c/Go/go` 会被 go 拒绝"relative GOPATH"）
- 建议 `go mod init <module>` 用单调模块名（如 `go-soul`），别用重名

### ⚠️ Go 服务内存缓存 index.html（最坑）
子代理写的 `loadIndex()` 用 package 级缓存：`if len(idxHTML)>0 && idxPath==webDir { return idxHTML }` ——**改前端 HTML 后必须重启 Go 进程**才生效，不然改了半天 curl 回来的还是旧版。调试现象：磁盘 html 是新代码、curl 是旧代码、浏览器 bodyHTML=0 全乱。
- **早发现**：改前端后 `curl -s localhost:8080/ | grep "新标记"` 验证，无则重启再试
- **根治**：开发期让 loadIndex 每次读文件，或加 `/api/reload` 清缓存

### HTML/JS 同文件前端
- 前端是把 HTML+CSS+JS 塞进一个 `.html`（Go 原样返回）。**改 JS 函数后怀疑"改了没生效"时，先 `.toString().includes(新代码)` 在 browser console 验证**——很可能是缓存旧 JS 而非逻辑错
- option 填充判断坑：判断"首次填充"用 `select.options.length<=1`（初始有 1 个占位 option），用 `!select.querySelector('option')` 会因占位 option 永远为 false 导致永不填充

### 纯工具容器 vs Web 容器
- Flask 容器入口默认跑 Web 占 8080。Go 版要独立跑宿主机 exe + **纯工具容器**（工具执行 `docker exec` 目标）：`docker run -d --name hexagent-kali-tools --entrypoint sleep hexagent-hexagent:latest infinity`
- Go exe 启动时用环境变量指定容器：`HEXAGENT_KALI=hexagent-kali-tools ./kurisulab-soul.exe`

### Docker 状态缓存
每次 API 调 `docker inspect` 很慢（几百 ms）。用后台 goroutine 每 30s 刷新一次 `dockerUp` 缓存 + RWMutex，API 就 <10ms 了。

### Go 工具执行（os/exec 双重源头）
```go
fullCmd := fmt.Sprintf("docker exec %s bash -c '%s'", container, strings.ReplaceAll(cmd, "'", "'\\''"))
c := exec.Command("bash", "-c", fullCmd) // Windows 下要包 bash -c 才能管道+socket
```
工具命令占位符 `{t}` 用 `strings.ReplaceAll(tool.Cmd, "{t}", target)` 渲染。

### 白盒审计 JSON 三级回退（同 Python 版）
小模型输出不保证严格 JSON（可能 `=>` 或 `<|im_start|>`）：
1. `json.Unmarshal` 全文 → 2. regexp 提取 `{...vulnerabilities...}` 块 → 3. 纯文本 CWE/关键词扫描回填

## References

- `references/hexagent-web-dashboard.md` — HexAgent 完整架构参考
- `references/embedded-flask-dashboard.md` — Flask 内嵌仪表盘验证闭环
