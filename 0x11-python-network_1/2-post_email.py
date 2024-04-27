#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter and 
    displays the body of the response (decoded in utf-8).

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to be sent as a parameter in the POST request.

    Returns:
        str: The body of the response (decoded in utf-8).
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        return body

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print(response_body)

