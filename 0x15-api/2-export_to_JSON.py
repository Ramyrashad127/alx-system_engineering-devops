#!/usr/bin/python3


"""import modules"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}")
    name = tasks.json().get('name')
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    ans = data.json()
    file = f"{id}.json"
    utasks = {}
    tasks = []
    dic = {}
    with open(file, 'w') as f:
        for ele in ans:
            dic['task'] = ele.get('task')
            dic['completed'] = ele.get('task')
            dic['username'] = ele.get('username')
            tasks.append(dic)
        utasks[id] = tasks
        json.dump(utasks, f)
