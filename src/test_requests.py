import requests


def fetch_github_status():
    url = "https://api.github.com"
    try:
        response = requests.get(url, timeout=5)
        print(f"[*]Status Code: {response.status_code}")
        data = response.json()
        print(f"[+] Successfully connected to: {data['current_user_url']}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Network Error: {e}")


if __name__ == "__main__":
    fetch_github_status()
