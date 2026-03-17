tasks = []

def add_task():
    print("")
    task = input("What is the task? ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    print("")
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("")
        try:
            remove = int(input("Which task do you want to remove? "))
            if 1 <= remove <= len(tasks):
                tasks.pop(remove - 1)
                print("Task removed!")
            else:
                print("Invalid!")
        except ValueError:
            print("Invalid! Please enter a number!")
            return
        
def done_task():
    print("")
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("")
        try:
            done = int(input("Which task did you done?(in number) "))
            if 1 <= done <= len(tasks):
                tasks[done - 1] = tasks[done - 1] + " ✅"
                print("Task is done!")
            else:
                print("Invalid!")
        except ValueError:
            print("Invalid! Please enter a number!")

def list_tasks():
    print("")
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n1 - Add task")
    print("2 - Remove task")
    print("3 - List your tasks")
    print("4 - Done your tasks")
    print("5 - Exit")

    choice = input("What is your choice? ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        list_tasks()
    elif choice == "4":
        done_task()
    elif choice == "5":
        print("Ok, bye!")
        break
    else:
        print("Invalid")

