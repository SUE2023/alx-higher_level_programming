#!/usr/bin/python3
import requests
import sys

def fetch_request_id(url):
    """
    Sends a request to the specified URL and displays the value of the variable X-Request-Id 
    in the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable.
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id

if __name__ == "__main__":
    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)

