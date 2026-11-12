import re
def extract_flag(log_data):
# 目标： 从一堆乱七八糟的文本里提取出 flag{...}
# 正则表达式解释： 匹配 flag{开头，后面跟着任意字符（非贪婪模式），直到遇到}结尾
    pattern = r"flag\{[^}]+\}"
    match = re.search(pattern, log_data)
    if match:
        return match.group(0)
    return None

if __name__ == "__main__":
    fake_log = "System booting... Error at 0x41. SUCCESS! Here is your prize: flag{h4ck_th3_world}. All systems operational."

    print(extract_flag(fake_log))
    
