#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.Javascript should count as javascript, but java should not
"""

import requests


def count_words(subreddit, word_list, results=None, after=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        results (dict): A dictionary to store the keyword counts
        (initially empty).after (str): The "after" parameter to paginate
        through results(initially None).

    Returns:
        None
    """
    if results is None:
        results = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after is not None:
        url += f"&after={after}"

    headers = {
        "User-Agent": "MyRedditBot/1.0 (by YourUsername)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            words = title.split()
            for word in words:
                word = word.lower()
                word = word.strip('.,!?()[]{}"\'')
                if word in word_list:
                    if word in results:
                        results[word] += 1
                    else:
                        results[word] = 1
        after = data["data"]["after"]
        if after is not None:
            return count_words(subreddit, word_list, results, after)
        else:
            print_results(results)
    else:
        pass

def print_results(results):
    """
    Prints the sorted count of keywords from the results dictionary.

    Args:
        results (dict): A dictionary containing keyword counts.
    """
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_results:
        print(f"{word}: {count}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        keyword_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit_name, keyword_list)
