import os
import platform
import getpass

def system_recon():
    print("[*] Starting System Reconnaissance...")
    print("-" * 40)

    # 1. Identity Check (Who am I?)
    # In a real attack, you want to know if you are root or a low-prilv user
    try:
        username = getpass.getuser()
        print(f"[*] Current User: {username}")
    except:
        print("[-] Could not determine user.")

    # 2. OS Information(What OS am I running?)
    # Knowing the kenel version and OS can help you determine what exploits may work
    print(f"[+] OS Type: {platform.system()}")
    print(f"[+] OS Release: {platform.release()}")
    print(f"[+] Machine: {platform.machine()}")

    # 3. Environment Variables (What environment am I running in?)
    # Sometimes environment variables can leak sensitive information like API keys or passwords
    print("\n[*] Scanning Environment Vriables...")
    for key, value in os.environ.items():
        if "secret" in key.lower() or "password" in key.lower() or "api" in key.lower()or "pass" in key.lower():
            print(f"[!] Potential Sensitive Data -> {key}: {value}")

    # 4. System Command Excution （The ultimate power)
    # Running native Linux commands directly from Python.
    print("\n[*] Executing shell commands...")

    #Let's check the current working directory and network info
    current_dir = os.popen("pwd").read().strip()
    print(f"[+] Current Dircotory: {current_dir}")

    # Check if netcat (nc) is installed and available
    nc_path = os.popen("which nc").read().strip()
    if nc_path:
        print(f"[+] Netcat is installed at: {nc_path}")
    else:
        print("[-] Netcat is not installed.")

    print("-" * 40)
    print("[*] Recon Complete.")
if __name__ == "__main__":
     system_recon()


        

