#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    e_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(e_id)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(e_id)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    employeename = employeeName.json()['name']

    total_tasks = 0

    for tasks_done in json_req:
        if tasks_done['completed']:
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employeename, total_tasks, len(json_req)))

    for tasks_done in json_req:
        if tasks_done['completed']:
            print("\t " + tasks_done.get('title'))
