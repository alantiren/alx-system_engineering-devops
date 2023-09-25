#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
import sys


if __name__ == "__main__":

    sessionReq = requests.Session()

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    employeename = employeeName.json()['name']

    total_tasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employeename, total_tasks,len(json_req)))

    for task in completed_tasks:
        print(f"\t{task['title']}")
