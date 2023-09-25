#!/usr/bin/python3
"""script to export data in the JSON format"""
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response_user = requests.get(user_url)
    user_data = response_user.json()
    user_id = user_data.get("id")
    username = user_data.get("username")

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todo = requests.get(todo_url)
    todo_data = response_todo.json()

    json_data = {user_id: [{"task": task.get("title"), "completed": task.get("completed"), "username": username} for task in todo_data]}

    json_filename = "{}.json".format(user_id)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to {}".format(json_filename))
