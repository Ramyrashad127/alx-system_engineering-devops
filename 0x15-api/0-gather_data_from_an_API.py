#!/usr/bin/python3


"""import modules"""
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
    done_tasks = []
    cnt_done = 0
    cnt_tot = 0
    for ele in ans:
        if ele.get('userId') == int(id):
            cnt_tot += 1
            if ele.get("completed"):
                cnt_done += 1
                done_tasks.append(ele.get('title'))
    print(f"Employee {name} is done with tasks({cnt_done}/{cnt_tot}):")
    for task in done_tasks:
        print(f"\t {task}")
