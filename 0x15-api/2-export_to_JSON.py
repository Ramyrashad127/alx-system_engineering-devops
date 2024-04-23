#!/usr/bin/python3


"""import modules"""
import requests
import sys
import json


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
        json.dump(tasks, f)

