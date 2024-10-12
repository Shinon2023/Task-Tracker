import json
import os
import datetime

current_time = datetime.datetime.now()
filename = 'data.json'

task = {
    "id": 0,
    "description": "",
    "status": "",
    "createdAt": "",
    "updatedAt": "",
}

def add(task, data, current_time, filename):
    task["id"] = len(data) + 1
    description = ""
    for i in range(len(event) - 1):
        description += " "+event[i + 1]
    task["description"] = description
    task["status"] = "todo"
    task["createdAt"] = str(current_time)
    task["updatedAt"] = str(current_time)
    if os.path.exists(filename):
        data.append(task)
    else:
        data = [task]

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def list(event, data):
    description = ["ID", "Description", "Status", "Created At", "Updated At"]
    print("-" * 119)
    print(f"|{description[0].center(8)}|{description[1].center(30)}|{description[2].center(15)}|{description[3].center(30)}|{description[4].center(30)}|")
    print("-" * 119)
    if len(event) == 1:
        for i in range(len(data)):
            print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
            print("-" * 119)
    elif len(event) > 1:
        if event[1] == "todo":
            for i in range(len(data)):
                if data[i]["status"] == "todo":
                    print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
                    print("-" * 119)
        elif event[1] == "in-progress":
            for i in range(len(data)):
                if data[i]["status"] == "in-progress":
                    print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
                    print("-" * 119)
        elif event[1] == "done":
            for i in range(len(data)):
                if data[i]["status"] == "done":
                    print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
                    print("-" * 119)
        else:
            for i in range(len(data)):
                print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
                print("-" * 119)

def mark (event, data, status, filename):
    data[int(event[1]) - 1]["status"] = status
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Task marked {status}.")
    
def delete (event, data, filename):    
    if event[1] == "all":
        data = []
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            print("All tasks deleted.")
    else:
        data.pop(int(event[1]) - 1)
        for i in range(len(data)):
            data[i]["id"] = i + 1
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            print("Task deleted.")

def help():
    print("Commands:")
    print("add <Description>".ljust(40) + ": add a new task")
    print("update <ID> <Description>".ljust(40) + ": update this task description")
    print("mark-in-progress <ID>".ljust(40) +": mark this task id as in progress")
    print("mark-done <ID>".ljust(40) + ": mark this task id as done")
    print("delete <ID>, all".ljust(40) + ": delete this task id or delete all tasks")
    print("list <status>".ljust(40) + ": list tasks")

def update (event, data, filename):
    description = ""
    for i in range(len(event) - 2):
        description += " "+ event[i + 2]
    data[int(event[1]) - 1]["description"] = description
    data[int(event[1]) - 1]["updatedAt"] = str(current_time)
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)           
        print("Task updated.")
            
while True:
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file) 
    event = input("Task Tracker... ")
    event = event.split(" ");
    if event[0] == "add":
        add(task, data, current_time, filename)
        list(event, data)
            
    elif event[0] == "mark-in-progress":
        mark(event, data, "in-progress", filename)
        list(event, data)
            
    elif event[0] == "mark-done":
        mark(event, data, "done", filename)
        list(event, data)
    
    elif event[0] == "delete":
        delete(event, data, filename)
        list(event, data)
    
    elif event[0] == "update":
        update(event, data, filename)
        list(event, data)
            
    elif event[0] == "list":
        list(event, data)
    
    elif event[0] == "help":
        help()
    
    elif event[0] == "exit":
        break