import json

task = {"Do homework": {
    "id": 1,
    "date": "2022-01-01",
    "time": "08:00",
    "status": "pending"  
}}

event_continue = True

def add_task(task):
    with open('data.json', 'w') as json_file:
        json.dump(task, json_file, indent=4)


while event_continue:
    id = len(task) + 1
    add_task(task)
    print("Task added")
    break