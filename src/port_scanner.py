import socket
import sys
from datetime import datetime

# 1. 获取目标
if len(sys.argv) == 2:
    target = sys.argv[1]
else:
    print("用法:python port_scanner.py <目标IP>")
    print("示例:python port_scanner.py 127.0.0.1")
    sys.exit(1)

print("-" * 50)
print("正在扫描目标: " + target)
print("扫描开始时间: " + str(datetime.now()))
print("-" * 50)

try:
    # 2. 把域名解析成IP地址
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("无法解析主机名")
    sys.exit(1)

# 3. 核心循环：扫描 1 到 1024 端口
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # 设置超时时间为0.5秒
    result = s.connect_ex((target_ip, port))  # 尝试连接端口
    if result == 0:
        print(f"端口 {port} 开放")
    s.close()

print("-" * 50)
print("扫描结束时间: " + str(datetime.now()))