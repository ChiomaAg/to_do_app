

````markdown
# 📝 Python CLI To-Do App

A lightweight command-line To-Do list manager written in Python.  
Manage your tasks from the terminal — add, update, delete, mark progress, and filter by status — all stored locally in a `tasks.json` file.

---

## ✨ Features

- ✅ Add tasks with descriptions
- 📋 List tasks by status (`todo`, `in_progress`, `done`, or `all`)
- ✏️ Update a task’s description by ID
- 🚧 Mark tasks as **in progress**
- ✔️ Mark tasks as **done**
- ❌ Delete tasks by ID
- 🕒 Automatically tracks `createdAt` and `updatedAt` timestamps
- 💾 Persistent local storage using JSON

---

## 🚀 Getting Started

### 1. Clone the Repo or Copy the Script

```bash
git clone https://github.com/yourusername/cli-todo-app.git
cd cli-todo-app
````

### 2. Make Sure Python Is Installed

```bash
python3 --version
```

### 3. Run the App

```bash
python3 todo.py [command]
```

---

## 🧾 Available Commands

| Command                         | Description                        |
| ------------------------------- | ---------------------------------- |
| `--add "description"`           | Add a new task                     |
| `--update ID "new description"` | Update a task's description by ID  |
| `--delete ID`                   | Delete a task by ID                |
| `--mark_done ID`                | Mark a task as **done**            |
| `--mark_in_progress ID`         | Mark a task as **in progress**     |
| `--list`                        | List all tasks                     |
| `--list todo`                   | List only tasks with `Todo` status |
| `--list done`                   | List only completed tasks          |
| `--list in_progress`            | List tasks currently in progress   |

> ⚠️ Only one command can be used at a time.

---

## 💡 Example Usage

```bash
# Add a new task
python3 todo.py --add "Finish homework"

# Update a task's description
python3 todo.py --update 3 "Finish math homework"

# Mark a task as done
python3 todo.py --mark_done 3

# Mark a task as in progress
python3 todo.py --mark_in_progress 2

# Delete a task
python3 todo.py --delete 3

# List all tasks
python3 todo.py --list

# List only completed tasks
python3 todo.py --list done
```

---

## 📂 How Tasks Are Stored

All data is stored in a file called `tasks.json`.
Each task has the following structure:

```json
{
  "id": 3,
  "description": "Do laundry",
  "status": "Todo",
  "createdAt": "2025-10-21T01:23:45",
  "updatedAt": "2025-10-21T01:23:45"
}
```

---

## 🛠️ Future Improvements

* [ ] `--clear_done` command to bulk delete completed tasks
* [ ] Add support for due dates and priorities
* [ ] Colored CLI output using `rich` or `colorama`
* [ ] SQLite support for larger datasets
* [ ] Unit tests and CI integration

---

## 👤 Author

Made with ❤️ and JSON by **Chioma**
This project was built to sharpen Python, CLI scripting, and backend logic skills.

---

## 📄 License

MIT License – feel free to fork and remix!

```

```
