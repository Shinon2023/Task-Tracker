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

while True:
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file) 
    event = input("Task Tracker... ")
    event = event.split(" ");
    if event[0] == "add":
        task["id"] = len(data) + 1
        task["description"] = event[1]
        task["status"] = "todo"
        task["createdAt"] = str(current_time)
        task["updatedAt"] = str(current_time)
        if os.path.exists(filename):
            data.append(task)
        else:
            data = [task]

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
    elif event[0] == "mark-in-progress":
        data[int(event[1]) - 1]["status"] = "in-progress"
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            print("Task marked in progress.")
            
    elif event[0] == "mark-done":
        data[int(event[1]) - 1]["status"] = "in-progress"
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            print("Task marked in progress.")
    
    elif event[0] == "delete":
        data.pop(int(event[1]) - 1)
        for i in range(len(data)):
            data[i]["id"] = i + 1
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            print("Task deleted.")
    
    elif event[0] == "update":
        data[int(event[1]) - 1]["description"] = event[2]
        data[int(event[1]) - 1]["updatedAt"] = str(current_time)
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)           
            print("Task updated.")
            
    elif event[0] == "list":
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
            if event[1] == "in-progress":
                for i in range(len(data)):
                    if data[i]["status"] == "in-progress":
                        print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
                        print("-" * 119)
            if event[1] == "done":
                for i in range(len(data)):
                    if data[i]["status"] == "done":
                        print(f"|{str(data[i]["id"]).center(8)}|{data[i]["description"][:30].center(30)}|{data[i]["status"].center(15)}|{data[i]["createdAt"].center(30)}|{data[i]["updatedAt"].center(30)}|")
                        print("-" * 119)
           
    elif event[0] == "exit":
        break