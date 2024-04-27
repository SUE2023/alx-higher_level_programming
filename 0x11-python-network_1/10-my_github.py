#!/usr/bin/python3
import requests
import sys

def get_github_id(username, password):
    """
    Uses the GitHub API to display the user's id using Basic Authentication with a personal access token.

    Args:
        username (str): The GitHub username.
        password (str): The personal access token as password.

    Returns:
        str: The user's id if the authentication is successful, otherwise None.
    """
    url = "https://api.github.com/user"
    auth = (username, password)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)


