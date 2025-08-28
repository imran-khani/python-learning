# A simple Todo list

print("Welcome to our Todo APP :)")

todos = []


def addTodo():
    todo = input("Enter todo title: ").strip()
    if todo:
        todos.append(todo)
        print("Your todo is added to the list.")
    else:
        print("Write a proper todo title.")


def showTodos():
    if not todos:
        print("No todos yet. Add one first!")
    else:
        print("\nYour Todos:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
    input("\nPress Enter to return to menu...")


def showMenu():
    print(
        """
    1. Add todo
    2. View all todos
    3. Exit program
    """
    )


def saveTodo():
    with open("todos.txt", "a") as file:
        for todo in todos:
            file.write(todo + "\n")


while True:
    showMenu()
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        addTodo()
    elif choice == "2":
        showTodos()
    elif choice == "3":
        print("Goodbye! :)")
        break
    else:
        print("Invalid choice. Please choose again.")
