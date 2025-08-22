import sys
import json
import os

TODO_FILE = "todo_data.json"

class TodoManager:
    def __init__(self, filename=TODO_FILE):
        self.filename = filename
        self.items = self.load()

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.items, f, indent=4)

    def add(self, task):
        self.items.append({'task': task, 'done': False})
        self.save()

    def list(self):
        for idx, item in enumerate(self.items, 1):
            status = "✓" if item['done'] else "✗"
            print(f"{idx}. [{status}] {item['task']}")

    def complete(self, index):
        try:
            self.items[index-1]['done'] = True
            self.save()
        except IndexError:
            print("Invalid item number.")

    def remove(self, index):
        try:
            removed = self.items.pop(index-1)
            self.save()
            print(f"Removed: {removed['task']}")
        except IndexError:
            print("Invalid item number.")

def print_help():
    print("Usage:")
    print("  python todo.py add \"Task Description\"")
    print("  python todo.py list")
    print("  python todo.py complete <task_number>")
    print("  python todo.py remove <task_number>")

if __name__ == "__main__":
    manager = TodoManager()
    if len(sys.argv) < 2:
        print_help()
    else:
        command = sys.argv[1]
        if command == "add" and len(sys.argv) >= 3:
            manager.add(sys.argv)
        elif command == "list":
            manager.list()
        elif command == "complete" and len(sys.argv) >= 3:
            manager.complete(int(sys.argv))
        elif command == "remove" and len(sys.argv) >= 3:
            manager.remove(int(sys.argv))
        else:
            print_help()
