#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as sam
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        employee = sam.get('{}/users/{}'.format(REST_API, id)).json()
        task_req = sam.get('{}/todos'.format(REST_API)).json()
        employee_name = employee.get('name')
        tasks = list(filter(lambda x: x.get('userId') == id, task_req))
        completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
        print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                len(completed_tasks), len(tasks)))
        if len(completed_tasks) > 0:
            for task in completed_tasks:
                print('\t{}'.format(task.get('title')))
