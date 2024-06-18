#!/usr/bin/python3


""" import modules """
import requests


def number_of_subscribers(subreddit):
    """new function """
    headers = {'User-Agent': "My-User-Agent"}
    response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json()['data']['subscribers']
