import json

tasks = []
new_task = ""

while True:
    print("Enter a new task to add a task, view to view your current tasks, done to remove a task or stop to exit")
    new_task = input("Enter: ")
    if new_task.lower() == "view":
        print(tasks)
    elif new_task.lower() == "done":
        print(tasks)
        remove = int(input("Enter number of python task to remove (starts at 1): "))
        remove -= 1
        tasks.pop(remove)
    elif new_task != "":
        tasks.append(new_task)