#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as sam
import sys

"""if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = sam.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = sam.get(url + 'todos', params={'userId': sys.argv[1]}).json()
#    print(to_do)
    completed = [title.get("title") for title in to_do if title.get('completed') is True]
    # print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),len(completed),len(to_do)))
    [print("\t {}".format(title)) for title in completed]"""


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
