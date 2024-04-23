#!/usr/bin/python3


"""import modules"""
import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}")
    uname = tasks.json().get('username')
    data = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    ans = data.json()
    file = f"{id}.csv"
    with open(file, 'w') as f:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for ele in ans:
            if ele.get('userId') == int(id):
                check = ele.get('completed')
                title = ele.get('title')
                writer.writerow([id, uname, check, title])
