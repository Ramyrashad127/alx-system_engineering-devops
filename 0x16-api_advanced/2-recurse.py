#!/usr/bin/python3


""" import """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ new """
    headers = {'User-Agent': 'My-User-Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
