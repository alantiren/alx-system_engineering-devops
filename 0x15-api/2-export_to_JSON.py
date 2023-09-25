#!/usr/bin/python3
"""script to export data in the JSON format"""

import requests
import json
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
    user = employeeName.json()['username']

    total_tasks = []
    updateUser = {}

    for all_empl in json_req:
        total_tasks.append(
            {
                "task": all_empl.get('title'),
                "completed": all_empl.get('completed'),
                "username": user,
            })
    updateUser[e_id] = total_tasks

    file_Json = e_id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
