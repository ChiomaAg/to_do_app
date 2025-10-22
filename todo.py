import argparse
import json

parser = argparse.ArgumentParser(description="A CLI todo app")

# -----------------------Arguments------------------------------------
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--add", help="Adds a task to the to-do list")
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

# -----------------helpers-------------------------------------
args = parser.parse_args()
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


def save_data():
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)


# ---------------------main logic---------------------------------------------------
if args.add:
    task = args.add
    data_to_save = {
        "task": task,
        "status": ""
    }
    data.append(data_to_save)

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

    index = len(data)

    print(f'Task successfully added (ID: {index})')

elif args.update:
    index, task = args.update
    error_check(index)
    index = int(index) - 1
    if index > (len(data)-1):
        print("No task with that ID")
    else:
        data[index]["task"] = task
        save_data()

elif args.delete:
    index = args.delete
    error_check(index)
    index = int(index) - 1
    if index > (len(data)-1):
        print("No task with that ID")
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

else:
    print("Nothing to do")
