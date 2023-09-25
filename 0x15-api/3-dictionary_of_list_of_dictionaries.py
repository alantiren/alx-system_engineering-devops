#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get('username')

    user_tasks = []
    for task in tasks_data:
        task_data = {
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed'),
        }
        user_tasks.append(task_data)

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump({user_id: user_tasks}, json_file)
