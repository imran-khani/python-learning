# A Todo App with CRUD operations
import json

print("Welcome to our Todo APP :)")


def loadTodos():
    global todos
    try:
        with open("todos.json", "r") as file:
            todos = json.load(file)
    except FileNotFoundError:
        todos = []


loadTodos()


def addTodo():
    title = input("Enter todo title: ").strip()
    if title:
        todos.append({"title": title, "done": False})
        print("Your todo is added to the list.")
        saveTodo()
    else:
        print("Write a proper todo title.")


def markTodo():
    showTodos()
    try:
        num = int(input("Enter the number of todo you want to update status for: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = not todos[num - 1]["done"]
            saveTodo()
        else:
            print("invalid Number")
    except ValueError:
        print("Please enter a valid number")


def editTodo():
    showTodos()
    try:
        num = int(input("Enter the number of todo you want to edit: "))
        if 1 <= num <= len(todos):
            new_title = input("Enter new title for selected Todo: ").strip()
            if new_title:
                todos[num - 1]["title"] = new_title
                saveTodo()
                print("Todo edited successfully!")
            else:
                print("Title can't be empty...")
        else:
            print("invalid number")

    except ValueError:
        print("Enter proper number to select todo")


def showTodos():
    if not todos:
        print("No todos yet. Add one first!")
    else:
        print("\nYour Todos:")
        for i, todo in enumerate(todos, 1):
            status = "[x]" if todo["done"] else "[ ]"
            print(f"{i}. {status} {todo['title']}")
    input("\nPress Enter to return to menu...")


def deleteTodo():
    showTodos()
    try:
        num = int(input("Enter todo number to Delete: "))
        if 1 <= num <= len(todos):
            deleted = todos.pop(num - 1)
            saveTodo()
            print(f'The todo "{deleted["title"]}" is deleted.')
        else:
            print("invalid choice. try again")
    except ValueError:
        print("Please enter a valid number")


def showMenu():
    print(
        """
    1. Add todo
    2. View all todos
    3. Exit program
    4. Delete Todo
    5. Edit Todo
    """
    )


def saveTodo():
    with open("todos.json", "w") as file:
        json.dump(todos, file)


while True:
    showMenu()
    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        addTodo()
    elif choice == "2":
        showTodos()
    elif choice == "3":
        print("Goodbye! :)")
        break
    elif choice == "4":
        deleteTodo()
    elif choice == "5":
        editTodo()
    else:
        print("Invalid choice. Please choose again.")
