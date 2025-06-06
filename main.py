import time

tasks=[]
done_tasks=[]
index = 1

def add_function():
    function_to_add = input("Fill this land with task you want to add:")
    tasks.append(function_to_add)
    print(tasks)
    time.sleep(1)

def mark_as_done():
    print(tasks)
    m_as_done = int(input("Choose which task you want to mark as done"))
    tasks = done_tasks.copy(m_as_done)
    print(tasks)


def delete_tasks():
    print(tasks)
    delete_task = int(input("Choose which ToDo you want to delete:"))
    tasks.remove(delete_task)
    print(tasks)

def list_tasks():
    if not tasks:
        print("Your ToDo list is empty!")
        time.sleep(1)
    else:
        print(tasks)
        time.sleep(1)

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
        print("4. Mark as done")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_function()
        elif choice == "2":
            if not tasks:
                print("Your ToDo list is empty")
                time.sleep(1)
            else:
                delete_tasks()
                time.sleep(1)

        elif choice == "3":
            list_tasks()
            time.sleep(1)
        elif choice == "4":
            mark_as_done()
        elif choice == "5":
            exit_command()
        else:
            print("Invalid input. Please try again.")
