#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'my own custom header'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
