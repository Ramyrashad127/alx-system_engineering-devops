#!/usr/bin/python3


""" import modules """
import requests


def number_of_subscribers(subreddit):
    """new function """
    headers = {'User-Agent': "user-Agent"}
    response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
