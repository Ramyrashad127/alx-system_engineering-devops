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
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    data = data.json()
    for user in tasks:
        taskList = []
        for task in data:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        utasks[user.get('id')] = taskList
    file = "todo_all_employees.json"
    with open(file, 'w') as f:
        json.dump(utasks, f)
