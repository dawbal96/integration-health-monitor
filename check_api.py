import requests


def check_api(url):
    response = requests.get(url, timeout=10)

    print("URL:", url)
    print("Status code:", response.status_code)
    print("Time taken:", response.elapsed.total_seconds(), "seconds")

    if response.status_code == 200:
        print("Result: SUCCESS")
    else:
        print("Result: FAILURE")
    print("-" * 40)


check_api("https://api.github.com")
check_api("https://api.github.com/this-does-not-exist")
