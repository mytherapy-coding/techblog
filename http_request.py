import urllib.request

def send_get_request(url):
    try:
        with urllib.request.urlopen(url) as response:
            print("HTTP Status Code:", response.getcode())
            print("Response:")
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: {e}")


url = "https://google.com"
send_get_request(url)
