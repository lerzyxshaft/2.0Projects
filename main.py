tasks=[]

def add_function():
    function_to_add = input("Fill this land with task you want to add:")
    tasks.append(function_to_add)
    print(tasks)

def delete_tasks():
    delete_task = input("Choose which funktion you want to delete:")
    tasks.remove(delete_task)
    print(tasks)

def list_tasks():
    print(tasks)

def exit_command():
    quit()

if __name__=="__main__":
    print("Welcome to the ToDo list app :")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add the task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice")

        if choice == "1":
            add_function()
        elif choice == "2":
            delete_tasks()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            exit_command()
        else:
            print("Invalid input. Please try again.")
