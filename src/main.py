import pprint

import requests


def main():
    response = requests.get("https://dummyjson.com/users", timeout=1)
    response.raise_for_status()
    data = response.json()
    pprint.pprint(data)


if __name__ == "__main__":
    main()
