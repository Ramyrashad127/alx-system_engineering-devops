#!/usr/bin/python3


""" import modules """
import requests


def top_ten(subreddit):
    """ new """
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(
            'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
            headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])
