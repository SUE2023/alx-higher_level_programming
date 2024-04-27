#!/usr/bin/python3
import requests
import sys

def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the provided letter as a parameter.
    Displays the id and name from the response if JSON is properly formatted and not empty.

    Args:
        letter (str): The letter to be sent as a parameter in the POST request.

    Returns:
        None
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    search_user(letter)

