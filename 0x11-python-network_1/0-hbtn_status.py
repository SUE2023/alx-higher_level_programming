#!/usr/bin/python3
import urllib.request

def fetch_and_display():
    """
    Fetches the content of https://alx-intranet.hbtn.io/status
    and displays its body.

    Uses urllib package.

    Returns:
        None
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body_bytes = response.read()
        body_utf8 = body_bytes.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body_bytes))
    print("\t- content:", body_bytes)
    print("\t- utf8 content:", body_utf8)

# This will only execute if the script is run directly, not when it's imported
if __name__ == "__main__":
    fetch_and_display()


