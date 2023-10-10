#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "MyRedditBot/1.0 (by YourUsername)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
