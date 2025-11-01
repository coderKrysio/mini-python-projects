tasks=[]

print("Welcome to the To-Do List App!")

def print_menu():
    print("*****\nMenu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
def print_tasks():
    print("Your Tasks:")
    for i in range(tasks.__len__()):
        print(f"{i + 1}. {tasks[i]}")

while True:
    print_menu()
    
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        if tasks.__len__() == 0:
            print("No tasks in the list.")
        else:
            print_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == '3':
        if tasks.__len__() == 0:
            print("No tasks to remove.")
        else:
            print_tasks()
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= tasks.__len__():
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
    elif choice == '4':
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")