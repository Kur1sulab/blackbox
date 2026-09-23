# blackbox

黑盒安全测试技能集，给 AI Agent 用的外部攻击/渗透测试 playbook 合集，共 144 个技能，按攻击链组织。

不看源码的视角：从外部侦察和攻击面测绘，到漏洞利用、权限提升、横向移动。每个技能是一份独立 playbook（触发条件/操作步骤/工具命令/坑位备忘），Claude Code、Hermes 等支持 Skills 的 Agent 可以直接加载。


## 技能索引

### 侦察与攻击面测绘（14）

| 技能 | 说明 |
|------|------|
| [hack-api-recon-and-docs](./hack-api-recon-and-docs/) | API reconnaissance and documentation review playbook |
| [hack-insecure-source-code-management](./hack-insecure-source-code-management/) | Source control and artifact exposure (.git, .svn, .hg, backups, .env) |
| [hack-recon-and-methodology](./hack-recon-and-methodology/) | Reconnaissance and methodology playbook |
| [hack-recon-for-sec](./hack-recon-for-sec/) | Entry P1 category router for reconnaissance and methodology |
| [hack-subdomain-takeover](./hack-subdomain-takeover/) | Subdomain takeover detection and exploitation playbook |
| [hunt-recon-methodology](./hunt-recon-methodology/) | Recon methodology for bug bounty — subdomain enumeration, tech detection… |
| [linux-vuln-discovery](./linux-vuln-discovery/) | Linux安全漏洞发现与渗透测试技能 - 自适应决策框架 |
| [pt-osint](./pt-osint/) | Open-source intelligence gathering - company repository enumeration, sec… |
| [pt-patt-fetcher](./pt-patt-fetcher/) | Fetches and extracts payloads from PayloadsAllTheThings on demand. Bake… |
| [pt-reconnaissance](./pt-reconnaissance/) | Domain assessment and web application mapping - subdomain discovery, por… |
| [pt-techstack-identification](./pt-techstack-identification/) | OSINT-based technology stack identification. Routes to 6 domain sub-skil… |
| [web-frontend-recon](./web-frontend-recon/) | 前端 JS 侦察与 API 面提取方法——SPA fallback 识别、webpack chunk 接口提取、统一鉴权特征识别、OAuth/S… |
| [web-spa-recon](./web-spa-recon/) | SPA 前端侦察——从 Vue/React 单页应用提取真实 API 攻击面。识别 SPA fallback、拉取 JS chunk 提取接口定… |
| [lan-device-recon](./lan-device-recon/) | Windows 内网设备枚举与路由器侦察（ARP/端口/网关指纹） |

### 注入类漏洞（26）

| 技能 | 说明 |
|------|------|
| [hack-cmdi-command-injection](./hack-cmdi-command-injection/) | Command injection playbook |
| [hack-crlf-injection](./hack-crlf-injection/) | CRLF injection playbook |
| [hack-csv-formula-injection](./hack-csv-formula-injection/) | CSV/spreadsheet formula injection (DDE, Excel/LibreOffice, Google Sheets… |
| [hack-dangling-markup-injection](./hack-dangling-markup-injection/) | Dangling markup injection playbook |
| [hack-deserialization-insecure](./hack-deserialization-insecure/) | Insecure deserialization playbook |
| [hack-email-header-injection](./hack-email-header-injection/) | Email header injection and spoofing playbook |
| [hack-expression-language-injection](./hack-expression-language-injection/) | Expression Language injection playbook |
| [hack-format-string-exploitation](./hack-format-string-exploitation/) | Format string exploitation playbook |
| [hack-ghost-bits-cast-attack](./hack-ghost-bits-cast-attack/) | Java "Ghost Bits" / Cast Attack playbook (Black Hat Asia 2026) |
| [hack-graphql-and-hidden-parameters](./hack-graphql-and-hidden-parameters/) | GraphQL and hidden parameter testing playbook |
| [hack-http-host-header-attacks](./hack-http-host-header-attacks/) | HTTP Host header injection and routing abuse playbook |
| [hack-http-parameter-pollution](./hack-http-parameter-pollution/) | HTTP Parameter Pollution (HPP): duplicate query/body keys parsed differe… |
| [hack-http2-specific-attacks](./hack-http2-specific-attacks/) | HTTP/2 protocol-specific attack playbook |
| [hack-injection-checking](./hack-injection-checking/) | Entry P1 category router for injection testing |
| [hack-jndi-injection](./hack-jndi-injection/) | JNDI injection playbook |
| [hack-llm-prompt-injection](./hack-llm-prompt-injection/) | LLM prompt injection playbook |
| [hack-macos-process-injection](./hack-macos-process-injection/) | macOS process injection playbook |
| [hack-prototype-pollution](./hack-prototype-pollution/) | Prototype pollution testing for JavaScript stacks |
| [hack-prototype-pollution-advanced](./hack-prototype-pollution-advanced/) | Advanced prototype pollution playbook — server-side RCE, client-side gad… |
| [hack-sqli-sql-injection](./hack-sqli-sql-injection/) | SQL injection playbook |
| [hack-ssrf-server-side-request-forgery](./hack-ssrf-server-side-request-forgery/) | SSRF playbook |
| [hack-ssti-server-side-template-injection](./hack-ssti-server-side-template-injection/) | SSTI playbook |
| [hack-websocket-security](./hack-websocket-security/) | WebSocket handshake, CSWSH, tooling (wsrepl, ws-harness, Burp), and comm… |
| [hack-xslt-injection](./hack-xslt-injection/) | XSLT injection testing: processor fingerprinting, XXE and document() SSR… |
| [hack-xxe-xml-external-entity](./hack-xxe-xml-external-entity/) | XXE playbook |
| [pt-injection](./pt-injection/) | Injection vulnerability testing - SQL, NoSQL, OS Command, SSTI, XXE, and… |

### Web 应用与客户端（20）

| 技能 | 说明 |
|------|------|
| [api-security-testing](./api-security-testing/) | API安全测试 — 基于《Secure APIs》(Manning 2025)和OWASP API Top 10。覆盖Swagger发现、Gra… |
| [hack-clickjacking](./hack-clickjacking/) | Clickjacking playbook |
| [hack-cors-cross-origin-misconfiguration](./hack-cors-cross-origin-misconfiguration/) | CORS misconfiguration testing playbook |
| [hack-csp-bypass-advanced](./hack-csp-bypass-advanced/) | Advanced Content Security Policy bypass techniques |
| [hack-csrf-cross-site-request-forgery](./hack-csrf-cross-site-request-forgery/) | CSRF testing playbook |
| [hack-file-access-vuln](./hack-file-access-vuln/) | Entry P1 category router for file access and upload workflows |
| [hack-open-redirect](./hack-open-redirect/) | Open redirect playbook |
| [hack-path-traversal-lfi](./hack-path-traversal-lfi/) | Path traversal and LFI playbook |
| [hack-race-condition](./hack-race-condition/) | Race condition and TOCTOU testing for web apps |
| [hack-request-smuggling](./hack-request-smuggling/) | HTTP request smuggling and desynchronization testing |
| [hack-type-juggling](./hack-type-juggling/) | PHP type juggling and weak comparison (`==`) bypass |
| [hack-web-cache-deception](./hack-web-cache-deception/) | Web cache deception and poisoning playbook |
| [hack-xss-cross-site-scripting](./hack-xss-cross-site-scripting/) | XSS playbook |
| [hunt-hunt-xss](./hunt-hunt-xss/) | Hunting skill for Cross-Site Scripting (XSS) — DOM-based, stored, reflec… |
| [pt-api-security](./pt-api-security/) | API security testing - GraphQL, REST API, WebSocket, and Web-LLM attack… |
| [pt-client-side](./pt-client-side/) | Client-side vulnerability testing - XSS (reflected/stored/DOM), CSRF, CO… |
| [pt-server-side](./pt-server-side/) | Server-side vulnerability testing - SSRF, HTTP Request Smuggling, Path T… |
| [pt-web-app-logic](./pt-web-app-logic/) | Web application logic testing - business logic flaws, race conditions, a… |
| [web-app-security](./web-app-security/) | Web应用安全测试三柱法 — 基于Andrew Hoffman《Web Application Security 2nd》(O'Reilly 2… |
| [django-drf-pentest](./django-drf-pentest/) | 黑盒测试 Django/DRF 后端（DEBUG 取证 / 越权矩阵 / 上传 / JWT 爆破） |

### 认证、授权与令牌（15）

| 技能 | 说明 |
|------|------|
| [hack-401-403-bypass-techniques](./hack-401-403-bypass-techniques/) | 401/403 bypass playbook |
| [hack-api-auth-and-jwt-abuse](./hack-api-auth-and-jwt-abuse/) | API authentication and JWT abuse playbook |
| [hack-api-authorization-and-bola](./hack-api-authorization-and-bola/) | API authorization and BOLA testing playbook |
| [hack-auth-sec](./hack-auth-sec/) | Entry P1 category router for authentication and authorization |
| [hack-authbypass-authentication-flaws](./hack-authbypass-authentication-flaws/) | Authentication bypass testing playbook |
| [hack-hash-attack-techniques](./hack-hash-attack-techniques/) | Hash attack playbook |
| [hack-idor-broken-object-authorization](./hack-idor-broken-object-authorization/) | IDOR and broken object authorization testing playbook |
| [hack-jwt-oauth-token-attacks](./hack-jwt-oauth-token-attacks/) | JWT and OAuth token attack playbook |
| [hack-oauth-oidc-misconfiguration](./hack-oauth-oidc-misconfiguration/) | OAuth and OIDC misconfiguration testing playbook |
| [hack-saml-sso-assertion-attacks](./hack-saml-sso-assertion-attacks/) | SAML SSO assertion attack playbook |
| [hunt-hunt-idor](./hunt-hunt-idor/) | Hunting skill for Insecure Direct Object Reference / Broken Object Level… |
| [hunt-hunt-oauth](./hunt-hunt-oauth/) | Hunting skill for OAuth 2.0 / 2.1, OpenID Connect (OIDC), SAML SSO, and… |
| [jwt-static-key-bruteforce](./jwt-static-key-bruteforce/) | JWT HS256 静态密钥离线爆破 |
| [pt-authenticated-session-acquisition](./pt-authenticated-session-acquisition/) | Acquire an authenticated session THROUGH MFA/OTP on an in-scope target a… |
| [pt-authentication](./pt-authentication/) | Authentication security testing - auth bypass, JWT attacks, OAuth flaws,… |

### SRC 狩猎与业务逻辑（14）

| 技能 | 说明 |
|------|------|
| [hack-business-logic-vuln](./hack-business-logic-vuln/) | Entry P1 category router for business logic testing |
| [hack-business-logic-vulnerabilities](./hack-business-logic-vulnerabilities/) | Business logic vulnerability playbook |
| [hack-defi-attack-patterns](./hack-defi-attack-patterns/) | DeFi attack pattern playbook |
| [hunt-hunt-business-logic](./hunt-hunt-business-logic/) | Hunting skill for business-logic vulnerabilities (CWE-840 Business Logic… |
| [hunt-hunt-info-disclosure](./hunt-hunt-info-disclosure/) | Hunting skill for Information Disclosure / Sensitive Data Exposure (CWE-… |
| [hunt-hunt-llm-ai](./hunt-hunt-llm-ai/) | Hunting skill for LLM and Agentic AI vulnerabilities — direct + indirect… |
| [hunt-hunt-rce](./hunt-hunt-rce/) | Hunting skill for remote code execution. Built from 1,218 public RCE bug… |
| [hunt-hunting-methodology](./hunt-hunting-methodology/) | Hunting methodology — 5-phase non-linear bug bounty workflow (understand… |
| [hunt-report-writing](./hunt-report-writing/) | Bug bounty report writing — structure, evidence, severity, reproduction… |
| [hunt-triage-validation](./hunt-triage-validation/) | Triage and validation of hunting findings — dedupe, reproduce, verify ex… |
| [hunt-vuln-classes](./hunt-vuln-classes/) | Vulnerability class knowledge base for hunting — common bug classes, whe… |
| [pt-blockchain-security](./pt-blockchain-security/) | Smart contract security testing and blockchain CTF exploitation |
| [pt-hackerone](./pt-hackerone/) | HackerOne bug bounty automation - parses scope CSVs, deploys parallel pe… |
| [src-hunter-skill](./src-hunter-skill/) | 实战 SRC / 众测 / Bug bounty 漏洞挖掘工作流 skill。包含：5 阶段方法论（intake → recon → enum… |

### 系统提权与横向移动（13）

| 技能 | 说明 |
|------|------|
| [hack-arbitrary-write-to-rce](./hack-arbitrary-write-to-rce/) | Arbitrary write to RCE playbook |
| [hack-heap-exploitation](./hack-heap-exploitation/) | Heap exploitation playbook |
| [hack-kernel-exploitation](./hack-kernel-exploitation/) | Linux kernel exploitation playbook |
| [hack-linux-lateral-movement](./hack-linux-lateral-movement/) | Linux lateral movement playbook. Use after gaining initial access to piv… |
| [hack-linux-privilege-escalation](./hack-linux-privilege-escalation/) | Linux privilege escalation playbook |
| [hack-linux-security-bypass](./hack-linux-security-bypass/) | Linux security mechanism bypass playbook |
| [hack-macos-security-bypass](./hack-macos-security-bypass/) | macOS security bypass playbook |
| [hack-stack-overflow-and-rop](./hack-stack-overflow-and-rop/) | Stack overflow and ROP playbook |
| [hack-tunneling-and-pivoting](./hack-tunneling-and-pivoting/) | Tunneling and pivoting playbook |
| [hack-windows-av-evasion](./hack-windows-av-evasion/) | AV/EDR evasion playbook for Windows |
| [hack-windows-lateral-movement](./hack-windows-lateral-movement/) | Windows lateral movement playbook |
| [hack-windows-privilege-escalation](./hack-windows-privilege-escalation/) | Windows local privilege escalation playbook |
| [pt-system](./pt-system/) | System exploitation testing - Active Directory attacks, privilege escala… |

### Active Directory 与域渗透（5）

| 技能 | 说明 |
|------|------|
| [cobalt-strike-ops](./cobalt-strike-ops/) | Cobalt Strike 部署/启动/运维 |
| [hack-active-directory-acl-abuse](./hack-active-directory-acl-abuse/) | Active Directory ACL abuse playbook |
| [hack-active-directory-certificate-services](./hack-active-directory-certificate-services/) | AD Certificate Services attack playbook |
| [hack-active-directory-kerberos-attacks](./hack-active-directory-kerberos-attacks/) | Kerberos attack playbook for Active Directory |
| [hack-ntlm-relay-coercion](./hack-ntlm-relay-coercion/) | NTLM relay and authentication coercion playbook |

### 云、容器与供应链（8）

| 技能 | 说明 |
|------|------|
| [cloud-attack](./cloud-attack/) | 云安全攻击 — 覆盖AWS/阿里云/Azure/GCP。SSRF→Metadata→凭证窃取→横向移动→持久化。基于DEF CON 2026云安… |
| [cloudflare-browser-bypass](./cloudflare-browser-bypass/) | 用本机真实浏览器（Playwright + 本地 Chrome/Edge）绕过 Cloudflare Turnstile / 机器人检测， 访问… |
| [hack-container-escape-techniques](./hack-container-escape-techniques/) | Container escape playbook |
| [hack-dependency-confusion](./hack-dependency-confusion/) | Supply-chain testing via package-manager dependency confusion: when inte… |
| [hack-kubernetes-pentesting](./hack-kubernetes-pentesting/) | Kubernetes penetration testing playbook |
| [hack-sandbox-escape-techniques](./hack-sandbox-escape-techniques/) | Sandbox escape playbook |
| [pt-cloud-containers](./pt-cloud-containers/) | Cloud and container security testing - AWS, Azure, GCP, Docker, and Kube… |
| [redis-rogue-master-rce](./redis-rogue-master-rce/) | Redis 主从复制 RCE 完整打法与生产数据安全纪律。打 6379/Redis 凭据 |

### 移动端安全（4）

| 技能 | 说明 |
|------|------|
| [hack-android-pentesting-tricks](./hack-android-pentesting-tricks/) | Android pentesting playbook |
| [hack-ios-pentesting-tricks](./hack-ios-pentesting-tricks/) | iOS pentesting playbook |
| [hack-mobile-ssl-pinning-bypass](./hack-mobile-ssl-pinning-bypass/) | Mobile SSL pinning bypass playbook |
| [pt-mobile-security](./pt-mobile-security/) | Mobile application security testing (Android + iOS) mapped to OWASP MASV… |

### AI / LLM 安全（2）

| 技能 | 说明 |
|------|------|
| [pt-ai-threat-testing](./pt-ai-threat-testing/) | Offensive AI security testing and exploitation framework. Systematically… |
| [red-team-ai](./red-team-ai/) | AI驱动的红队实战指南 — 基于《Redefining Hacking》作者Omar Santos(DEF CON Red Team Villa… |

### 网络协议与边界设施（7）

| 技能 | 说明 |
|------|------|
| [hack-browser-exploitation-v8](./hack-browser-exploitation-v8/) | Browser and V8 exploitation playbook |
| [hack-dns-rebinding-attacks](./hack-dns-rebinding-attacks/) | DNS rebinding attack playbook |
| [hack-network-protocol-attacks](./hack-network-protocol-attacks/) | Network protocol attack playbook |
| [hack-waf-bypass-techniques](./hack-waf-bypass-techniques/) | WAF bypass methodology and generic evasion techniques |
| [pt-infrastructure](./pt-infrastructure/) | Network infrastructure testing - port scanning, DNS attacks, MITM, VLAN… |
| [pt-network-appliance-offensive](./pt-network-appliance-offensive/) | Offensive testing of perimeter network appliances and VPN crypto — IKE/I… |
| [safeline-waf-bypass](./safeline-waf-bypass/) | SafeLine WAF bypass testing |

### 社会工程（1）

| 技能 | 说明 |
|------|------|
| [pt-social-engineering](./pt-social-engineering/) | Social engineering testing - phishing, pretexting, vishing, and physical… |

### 方法论、框架与实战（15）

| 技能 | 说明 |
|------|------|
| [hack-api-sec](./hack-api-sec/) | Entry P1 category router for API security |
| [hack-hack](./hack-hack/) | Entry P0 primary router for HackSkills |
| [java-web-framework-pentest](./java-web-framework-pentest/) | Java Web 框架渗透实战手册——JeecgBoot/Shiro/RuoYi/SpringBoot fat jar 的指纹识别、攻击面地图与… |
| [jeecg-boot-deep-exploitation](./jeecg-boot-deep-exploitation/) | JeecgBoot 深入利用（双防线SQLi盲注/PBE凭据破解/接管/RCE判定） |
| [js-login-crypto-replica](./js-login-crypto-replica/) | 复刻登录页 JS 加密链为 Python 等价实现 |
| [pt-essential-tools](./pt-essential-tools/) | Core pentesting tools and methodology - Burp Suite usage, Playwright aut… |
| [pt-github-workflow](./pt-github-workflow/) | GitHub workflow automation — branching, committing, pushing, pull reques… |
| [pt-hackthebox](./pt-hackthebox/) | HackTheBox platform operations and automations to solve challenges, mach… |
| [pt-pentest-engagement](./pt-pentest-engagement/) | Run a professional penetration engagement OR a network vulnerability sca… |
| [rem-execution-boost](./rem-execution-boost/) | 雷姆执行增强模式（改编自 gpt-5.6-instruct v45 的"破甲提示词"机制，去毒化后适配 Hermes）。 核心：单任务聚焦 +… |
| [secknowledge-skill](./secknowledge-skill/) | Web+AI 安全测试知识库。融合 WooYun 88,636 案例 + 先知 L1-L4 方法论 + GAARM 173 风险 + OWASP… |
| [security-repo-learning](./security-repo-learning/) | 安全仓库采购与深度学习工作流 |
| [web-login-crypto-replica](./web-login-crypto-replica/) | 登录自动化需复刻 JS 加密链（RSAUtils/CAS）时用：node 跑真 JS 逐字节验证 Python 复刻 |
| [go-pentest-workbench-ops](./go-pentest-workbench-ops/) | 构建与运维 Go + Docker Kali + Ollama 多模型渗透工作台 |
| [security-agent-framework](./security-agent-framework/) | 构建 AI 驱动自动化渗透 Agent 框架（双模式 / 工具注册 / Docker Kali / Web 仪表盘） |

## 安装

方式一（Hermes CLI）：

```bash
hermes skills install <技能目录路径>
```

方式二（手动）：将技能目录复制到 Hermes skills 目录（如 `~/AppData/Local/hermes/skills/pentest/`），开新会话生效。

## 声明

本仓库所有内容仅供**授权范围内**的安全测试、本地靶场练习与安全研究使用。对未授权目标的主动测试行为与作者无关。
