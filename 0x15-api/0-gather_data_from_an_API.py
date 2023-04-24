#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as sam
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
       
    employee_name = sam.get(REST_API + "users/{}".format(sys.argv[1])).json()
    tasks = sam.get(REST_API + "todos", params={"userId":sys.argv[1]}).json()

    completed_tasks = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(employee_name.get('name'),
        len(completed_tasks), len(tasks)))
    [print("\t {}".format(c)) for c in completed_tasks]