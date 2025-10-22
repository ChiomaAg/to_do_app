import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser(description="A CLI todo app")

# -----------------------Arguments------------------------------------
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--add", help="Adds a task and description to the to-do list")
group.add_argument(
    "--update", nargs=2, help="Update a task using a given ID"
)
group.add_argument(
    '--delete', help="Deletes a task using a given ID"
)
group.add_argument(
    "--mark_in_progress", help="Marks a task in progress given an ID"
)
group.add_argument(
    "--mark_done", help="Marks a task as done given an ID"
)
group.add_argument(
    "--list", nargs="?", const="all", choices=["all", "done", "todo", "in_progress"], help="List all the tasks on the to-do list"
)

# -----------------helpers-------------------------------------
args = parser.parse_args()
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

try:
    with open("tasks.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []


def error_check(index):
    try:
        int_value = int(index)
    except ValueError:
        raise ValueError("The first argument should be an integer")


def find_index_by_id(data, task_id):
    for i, task in enumerate(data):
        if task["id"] == task_id:
            return i
    return None


def save_data():
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)


# ---------------------main logic---------------------------------------------------
if args.add:
    task = args.add
    index = len(data)

    data_to_save = {
        "id": index+1,
        "description": task,
        "status": "Todo",
        "createdAt": formatted_datetime,
        "updatedAt": formatted_datetime
    }
    data.append(data_to_save)

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f'Task successfully added (ID: {index+1})')

elif args.update:
    id, task = args.update
    id = int(id)
    index = find_index_by_id(data, id)
    if index is None:
        print("No task with that ID.")
    else:
        data[index]["description"] = task
        data[index]["updatedAt"] = formatted_datetime
        save_data()

elif args.delete:
    id = args.delete
    id = int(id)
    index = find_index_by_id(data, id)
    if index is None:
        print("No task with that ID.")
    else:
        del data[index]
        save_data()

elif args.mark_in_progress:
    index = args.mark_in_progress
    error_check(index)
    index = int(index) - 1
    if index > (len(data)-1):
        print("No task with that ID")
    else:
        data[index]["status"] = "In progress"
        save_data()

elif args.mark_done:
    index = args.mark_done
    error_check(index)
    index = int(index) - 1
    if index > (len(data)-1):
        print("No task with that ID")
    else:
        data[index]["status"] = "Done"
        save_data()

elif args.list:
    filter = args.list
    if filter == "all":
        print("Showing all tasks...")
        for item in data:
            print(item["description"])
    elif filter == "done":
        print("Showing completed tasks...")
        for item in data:
            if item["status"] == "Done":
                print(item["description"])
    elif filter == "todo":
        print("Showing todo tasks...")
        for item in data:
            if item["status"] == "Todo":
                print(item["description"])
    elif filter == "in_progress":
        print("Showing completed tasks...")
        for item in data:
            if item["status"] == "In progress":
                print(item["description"])
else:
    print("Nothing to do")
