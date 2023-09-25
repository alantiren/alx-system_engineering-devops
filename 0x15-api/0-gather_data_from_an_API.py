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
    employeename = user_data.get("name")

    todos_url = f"{base_url}todos"
    todos_params = {"userId": employee_id}
    todos_response = requests.get(todos_url, params=todos_params)
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task["completed"]]
    numcompleted_tasks = len(completed_tasks)
    totaltasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".
          format(employeename, numcompleted_tasks, totaltasks, len(json_req)))

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
