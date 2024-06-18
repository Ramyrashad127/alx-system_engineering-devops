#!/usr/bin/python3

""" import modules """
import requests

def number_of_subscribers(subreddit):
    """new function """
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects    =False)

    if response.status_code != 200:
        return 0

    return response.json()['data']['subscribers']
