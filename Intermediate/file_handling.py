# ------------------ Simple Use of file handling -------------- #

# with open("note.txt",'a') as f:
#     f.write("Hello file handling is easy in python \n")

# with open("note.txt",'r') as file:
#     content = file.read()
#     print(content)

# with open("note.txt","r") as file:
#     lines = file.readlines()

# total = len(lines)

# for i, line in enumerate(lines[-3:], start=total-2):
#     print(f"{i}:{line.strip()}" )


# --------------------- Learn Json file handling ----------------- #

# import json

# data = [
#     {
#         "name": "Imran",
#         "roll no": 34,
#         "class": 12
#     },
#       {
#         "name": "Khan",
#         "roll no": 39,
#         "class": 12
#     }
# ]

# with open("students.json",'r') as file:
#     json.load(file)

# with open("students.json",'w') as file:
#     json.dump(data,file, indent=4)


# ---------------------- Load data from API and save to json file ----------------


# import requests
# import json

# URI = "https://jsonplaceholder.typicode.com/todos"

# try:
#     print("Fetching data...")
#     data = requests.get(URI)

#     if data.status_code == 200:
#         response = data.json()

#         # collect only completed todos
#         final_todos = [todo for todo in response if todo["completed"]]

#         print(f"Found {len(final_todos)} completed todos.")
#         print("Saving to file...")

#         with open("todos.json", "w") as file:
#             json.dump(final_todos, file, indent=4)

#         print("Data saved to file.")
#     else:
#         print("Failed with status:", data.status_code)

# except Exception as e:
#     print("Data fetch failed:", e)


# -------------- working with CSV  -- ------------

# import csv

# city_to_find = input("Enter your city: ")

# contacts = [
#     {"name": "Alice", "phone": "1234567890", "city": "New York"},
#     {"name": "Bob", "phone": "9876543210", "city": "London"},
#     {"name": "Sara", "phone": "5556667777", "city": "New York"},
# ]

# with open("contacts.csv",'w', newline='') as file:
#     field_names = ["name","phone","city"]
#     writer = csv.DictWriter(file,fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(contacts)

# with open("contacts.csv",'r') as file:
#     reader = csv.DictReader(file)
#     found  = False

#     for row in reader:
#         if row["city"].lower() == city_to_find.lower():
#             print(f"Name: {row['name']}, Phone: {row['phone']}")
#             found  = True

#     if not found:
#         print("No matches found for this city name!")

import csv

students = [
    {"name": "Alice", "math": "85", "science": "90", "english": "88"},
    {"name": "Bob", "math": "78", "science": "82", "english": "85"},
    {"name": "Sara", "math": "92", "science": "88", "english": "95"},
]


with open("students.csv", "w", newline="") as file:
    field_names = ["name", "math", "science", "english"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(students)

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        math = int(row["math"])
        science = int(row["science"])
        english = int(row["english"])
        average = (math + english + science) / 3
        highest_average = 0
        top_student = ""
        if average > highest_average:
            highest_average = average
            top_student = row["name"]

print(f"\nTop student is {top_student} with an average of {highest_average:.2f}")
