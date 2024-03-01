import urllib.request
import ssl

def send_get_request(url):
    try:
        # Create an SSL context that doesn't verify certificates
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=context) as response:
            print("HTTP Status Code:", response.getcode())
            print("Response:")
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: {e}")

# Example usage with Google's homepage
url = "https://leetcode.com/"
send_get_request(url)
