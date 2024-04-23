#!/usr/bin/python3


"""import modules"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id))
    name = tasks.json().get("name")
    data =  requests.get(
        "https://jsonplaceholder.typicode.com/todos/{}".format(id))
    ans = data.json()
    done_tasks = []
    cnt_done = 0
    cnt_tot = 0
    for ele in ans:
        if ele.get('userId') == int(id):
            cnt_tot += 1
            if ele.get("completed"):
                cnt_done += 1
                done_tasks.append(ele.get("title"))
    print("Employee {} is done with tasks({}/{}}):"
          .format(name, cnt_done, cnt_tot))
    for task in done_tasks:
        print("\t{}".format(task))
if __name__ == "__main__":
    id = sys.argv[1]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id))
    name = tasks.json().get("name")
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos/{}".format(id))
    ans = data.json()
    done_tasks = []
    cnt_done = 0
    cnt_tot = 0
    for ele in ans:
        if ele.get('userId') == int(id):
            cnt_tot += 1
            if ele.get("completed"):
                cnt_done += 1
                done_tasks.append(ele.get("title"))
    print("Employee {} is done with tasks({}}/{}}):"
          .format(name, cnt_done, cnt_tot))
    for task in done_tasks:
        print("\t {}".format(task))

