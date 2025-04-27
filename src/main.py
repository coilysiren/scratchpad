import requests

if __name__ == "__main__":
    response = requests.get("http://ifconfig.me", timeout=1)
    response.raise_for_status()
    print(response.text)
    print(response)
