#!/usr/bin/python3
import requests
import sys

def fetch_commits(repository, owner):
    """
    Fetches 10 most recent commits of a given repository by a specified owner from the GitHub API.

    Args:
        repository (str): The name of the repository.
        owner (str): The owner of the repository.

    Returns:
        list: A list of tuples containing commit SHA and author name.
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[:10]  # Get the first 10 commits
        commits = [(commit['sha'], commit['commit']['author']['name']) for commit in data]
        return commits
    else:
        return None

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    commits = fetch_commits(repository, owner)
    if commits:
        for sha, author in commits:
            print(f"{sha}: {author}")
    else:
        print("Error fetching commits.")

