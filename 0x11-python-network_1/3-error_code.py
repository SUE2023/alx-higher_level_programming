#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

def display_response_body(url):
    """
    Sends a request to the specified URL and displays the body of the response (decoded in utf-8).
    Handles urllib.error.HTTPError exceptions and prints the HTTP status code.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)

if __name__ == "__main__":
    url = sys.argv[1]
    display_response_body(url)

