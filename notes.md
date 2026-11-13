# 🧠 Hacker's Cheat Sheet - Python & Linux 

> 这是我在自动化工具与底层安全学习中沉淀的“Cheat Sheet”。不记录基础语法，只记录实战中高频使用的代码片段。

## 1. 网络交互与伪装 (Requests)
在未来的 AI 红队测试或 Web 渗透中，伪装和异常处理是标配。

```python
import requests
# 伪装成浏览器（绕过基础 WAF）
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    # 强制设置超时，防止脚本卡死
    r = requests.get("https://api.target.com", headers=headers, timeout=5)
    if r.status_code == 200:
        data = r.json()  # 解析 JSON 格式的返回值
        print(data.get("key"))
except requests.exceptions.RequestException as e:
    print(f"[-] Network Error: {e}")
```

## 2. 文件遍历与情报提取 (OS & File I/O)
在做后渗透（Post-Exploitation）或挖源码漏洞时，用来找敏感文件。
```python
import os
# 递归遍历目录
for root, dirs, files in os.walk("/var/www/html"):
    for file in files:
        if file.endswith((".txt", ".log", ".php")):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    # 这里的 try-except 用来忽略无权限读取的文件
                    pass 
            except Exception:
                pass
            
```
## 3. 系统命令执行 (OS Popen)
拿到 Shell 后，在 Python 脚本里直接执行系统命令。

```python
import os
### 执行命令并获取输出（注意：在真实 Pwn 中，通常用 os.system 弹 shell）
output = os.popen("whoami").read().strip()
print(f"Current User: {output}")
### 检查目标机器有没有带 nc (netcat)
nc_path = os.popen("which nc").read().strip()
```

## 4. 正则提取 (Regex for Pwn / Logs)
在 Pwn 拿 Flag，或者分析极其混乱的日志时，正则是最快的手术刀。
```python
import re
### 典型的从乱码中提取 flag 的逻辑
log_text = "System booting... flag{th1s_1s_4_fl4g} ... cleaning up."
match = re.search(r"flag\{[^}]+\}", log_text)
if match:
    print(f"Got Flag: {match.group(0)}")
```

## 5. Pwn 脚本前置模板 (pwntools) - To be filled
(等我开始打 BUUCTF 的时候，这里会填满 pwntools 的神仙指令，比如 remote(), p64(), recvuntil() 等)

## 6. 常用 Linux/终端指令速查
find / -name "*.txt" 2>/dev/null : 查找文件，并忽略权限报错。

grep -rn "password" . : 递归查找当前目录下所有包含 password 的文件。

chmod +x ./binary : 给下载的 Pwn 题目二进制文件加执行权限。

file ./binary : 看文件是 64 位还是 32 位。