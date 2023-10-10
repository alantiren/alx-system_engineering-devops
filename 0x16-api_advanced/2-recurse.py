#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all
    hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The "after" parameter to paginate through results.

    Returns:
        list: A list containing the titles of all hot articles,
        or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot
.json?limit=100&after={after}"

    headers = {
        "User-Agent": "MyRedditBot/1.0 (by YourUsername)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)
        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
