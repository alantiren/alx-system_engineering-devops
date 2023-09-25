#!/usr/bin/python3
import requests
import sys
import csv

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
    user_name = user_data.get("username")

    # Fetch TODO list data
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todo = requests.get(todo_url)
    todo_data = response_todo.json()

    # Create and write data to CSV file
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })

    print("Data exported to {}".format(csv_filename))
