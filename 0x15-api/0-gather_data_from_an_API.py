#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_url = f"{base_url}todos"
    todos_params = {"userId": employee_id}
    todos_response = requests.get(todos_url, params=todos_params)
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    print("Employee {employee_name} is done with tasks({}/{}):".
          format(num_completed_tasks, total_tasks, len(json_req)))

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
