#!/usr/bin/python3


"""import modules"""
import json
import requests
import sys


if __name__ == "__main__":
    utasks = {}
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    tasks = tasks.json()
    for user in tasks:
        data = requests.get(
            "https://jsonplaceholder.typicode.com/todos")
        ans = data.json()
        file = "todo_all_employees.json"
        tasks = []
        dic = {}
        with open(file, 'a') as f:
            for ele in ans:
                dic['task'] = ele.get('title')
                dic['completed'] = ele.get('completed')
                dic['username'] = ele.get('username')
                tasks.append(dic)
            utasks[id] = tasks
            json.dump(utasks, f)
