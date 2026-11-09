import requests


def check_api(url):
    print("URL:", url)

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        print("Result: FAILURE")
        print("Error: Timeout (no response in time)")
        print("-" *40)
        return
    except requests.exceptions.ConnectionError:
        print("Result: FAILURE")
        print("Error: ConnectionError (could not connect)")
        print("-" *40)
        return

    print("Status code:", response.status_code)
    print("Time taken:", response.elapsed.total_seconds(), "seconds")

    if response.status_code == 200:
        print("Result: SUCCESS")
    else:
        print("Result: FAILURE")
    print("-" * 40)


urls = [
    "https://api.github.com",
    "https://this-domain-does-not-exist.invalid",
    "https://api.github.com/this-does-not-exist",
]

for url in urls:
    check_api(url)
