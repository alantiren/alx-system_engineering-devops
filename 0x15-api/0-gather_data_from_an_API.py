#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response_user = requests.get(user_url)
    user_data = response_user.json()
    employee_name = user_data.get("name")

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todo = requests.get(todo_url)
    todo_data = response_todo.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for task in todo_data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
