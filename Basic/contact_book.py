contacts = {}


def add_contact():
    name = input("Please Enter contact name: ")
    phone = input("Enter his Phone no. ")
    contacts[name] = phone
    print(f"Contact {name} added successfully!\n")


def showMenu():
    print(
        """
    1. Add contact
    2. View all contacts
    3. Search contact by name
    4. Update contact
    5. Delete contact
    6. Exit
"""
    )


def view_all_contacts():
    if not contacts:
        print("No contacts Found\n")
    else:
        for i, name in enumerate(contacts, 1):
            print(f"{i}. {name} - {contacts[name]}")
        print()


def search_with_name():
    if not contacts:
        print("No contacts found.\n")
    else:
        query = input("Enter contact name to search for: ")
        if query in contacts:
            print(f"{query} - {contacts[query]}\n")
        else:
            print("No contact found with this name.\n")


def update_contact():
    if not contacts:
        print("No contacts found.\n")
    else:
        view_all_contacts()
        index = int(input("Enter contact number to update: "))
        names = list(contacts.keys())
        if 1 <= index <= len(names):
            name = names[index - 1]
            new_number = input(f"Enter new phone number for {name}: ")
            contacts[name] = new_number
            print(f"{name}'s number updated successfully!\n")
        else:
            print("Invalid contact number.\n")


def delete_contact():
    if not contacts:
        print("No contacts found.\n")
    else:
        view_all_contacts()
        index = int(input("Enter contact number to delete: "))
        names = list(contacts.keys())
        if 1 <= index <= len(names):
            name = names[index - 1]
            contacts.pop(name)
            print(f"{name} deleted successfully!\n")
        else:
            print("Invalid contact number.\n")


while True:
    showMenu()
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_all_contacts()
    elif choice == 3:
        search_with_name()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid Choice. Please try again.\n")
