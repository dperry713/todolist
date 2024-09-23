def display_menu():
    """
    Displays the main menu options.
    """
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def main():
    display_menu()

if __name__ == "__main__":
    main()
def add_task(task_list):
    """
    Adds a task to the task list.
    """
    task_title = input("Enter the task title: ")
    task_list.append({"title": task_title, "status": "Incomplete"})
    print(f"Task '{task_title}' added successfully!")

def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            # Implement viewing tasks (coming up next!)
            pass
        elif choice == "3":
            # Implement marking a task as complete
            pass
        elif choice == "4":
            # Implement deleting a task
            pass
        elif choice == "5":
            print("Thank you for using our To-Do List App. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
def view_tasks(task_list):
    """
    Displays the list of tasks along with their titles and statuses.
    """
    print("\nYour Mighty To-Do List:")
    for idx, task in enumerate(task_list, start=1):
        print(f"{idx}. {task['title']} ({task['status']})")

def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)  # Ta-da! View tasks in action
        elif choice == "3":
            # Implement marking a task as complete
            pass
        elif choice == "4":
            # Implement deleting a task
            pass
        elif choice == "5":
            print("Thank you for using our To-Do List App. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
def mark_complete(task_list):
    """
    Marks a task as complete.
    """
    view_tasks(task_list)  # Display tasks for the user's convenience
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(task_list):
            task_list[task_number - 1]["status"] = "Complete"
            print(f"Task '{task_list[task_number - 1]['title']}' is now complete! 🎉")
        else:
            print("Invalid task number. Please choose a valid task.")
    except ValueError:
        print("Oops! That doesn't look like a valid task number. Please enter a numeric value.")

def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)  # Mark tasks as complete!
        elif choice == "4":
            # Implement deleting a task
            pass
        elif choice == "5":
            print("Thank you for using our To-Do List App. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
def delete_task(task_list):
    """
    Deletes a task from the task list.
    """
    view_tasks(task_list)  # Display tasks for the user's convenience
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(task_list):
            deleted_task_title = task_list.pop(task_number - 1)["title"]
            print(f"Task '{deleted_task_title}' has been deleted. Fare thee well! 🌟")
        else:
            print("Invalid task number. Please choose a valid task.")
    except ValueError:
        print("Oops! That doesn't look like a valid task number. Please enter a numeric value.")

def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)  # Deleting tasks—like a digital Marie Kondo!
        elif choice == "5":
            print("Thank you for using our To-Do List App. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using our To-Do List App. Have a great day!")
            break  # The grand exit!

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
