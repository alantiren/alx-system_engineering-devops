#!/usr/bin/python3
""" script to export data in the CSV format"""

import requests
import json
import csv
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

    total_tasks = 0

    for tasks_done in json_req:
        if tasks_done['completed']:
            total_tasks += 1

    fileCSV = e_id + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([e_id, user, i.get('completed'), i.get('title')])
