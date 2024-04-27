#!/usr/bin/python3
import requests

def fetch_and_display():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status using the requests package 
    and displays the body of the response with the required formatting.

    Returns:
        None
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    fetch_and_display()

