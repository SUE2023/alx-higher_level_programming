#!/usr/bin/python3
import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter and 
    displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to be sent as a parameter in the POST request.

    Returns:
        str: The body of the response.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print("Your email is:", email)
    print(response_body)

