# Task Tracker CLI

This is a simple command-line interface (CLI) task tracker written in Python. It allows you to add, update, mark as in-progress or done, delete, and list tasks. Tasks are stored in a JSON file (`data.json`).

## Features

- **Add a Task**: Add a new task with a description.
- **Update a Task**: Update the description of an existing task.
- **Mark Tasks**: Mark tasks as `in-progress` or `done`.
- **Delete Tasks**: Delete a specific task or all tasks.
- **List Tasks**: List tasks by status (`todo`, `in-progress`, `done`) or list all tasks.
- **Help Command**: Show available commands.

## Installation

1. Clone this repository or copy the script.
3. Install dependencies (if needed).
4. Run the script from the terminal.

## Usage

You can interact with the task tracker by typing commands into the terminal. Below are the available commands:

## Frist step

```bash
#clone this repo
git clone https://github.com/Shinon2023/Task-Tracker---Roadmap-Project.git
cd <path your project>
#use this env
.\env\Scripts\activate
#run this code
python index.python
#example
Task Tracker... help
```

output
```bash
Commands:
add <Description>                       : add a new task
mark-in-progress <ID>                   : mark this task id as in progress
mark-done <ID>                          : mark this task id as done
delete <ID>, all                        : delete this task id or delete all tasks
list <status>                           : list tasks
```

## File Structure
The task data is saved in data.json. Each task contains the following information:

- **id**: Unique identifier for each task.
- **description**: Description of the task.
- **status**: Status of the task (todo, in-progress, done).
- **createdAt**: The date and time the task was created.
- **updatedAt**: The last time the task was updated.

## Notes
- If data.json does not exist, the script will create one automatically.
- Task descriptions longer than 30 characters will be truncated in the task list display.

## License
This project is open-source and free to use.