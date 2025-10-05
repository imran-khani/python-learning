# ------------------ Simple Use of File Handling -------------- #

# # Open a file in append mode and write a line to it
# with open("note.txt", 'a') as f:
#     f.write("Hello file handling is easy in python \n")

# # Read the full content of the file and print it
# with open("note.txt", 'r') as file:
#     content = file.read()
#     print(content)

# # Read file line by line and print last 3 lines with line numbers
# with open("note.txt", "r") as file:
#     lines = file.readlines()

# total = len(lines)

# for i, line in enumerate(lines[-3:], start=total-2):
#     print(f"{i}:{line.strip()}")


# ------------------ Learn JSON File Handling ------------------ #

# import json

# # Sample data: list of students
# data = [
#     {"name": "Imran", "roll no": 34, "class": 12},
#     {"name": "Khan", "roll no": 39, "class": 12}
# ]

# # Load JSON from file (reading)
# with open("students.json", 'r') as file:
#     json.load(file)

# # Save data to a JSON file (writing)
# with open("students.json", 'w') as file:
#     json.dump(data, file, indent=4)


# ----------- Load Data from API and Save to JSON File ----------- #

# import requests
# import json

# URI = "https://jsonplaceholder.typicode.com/todos"

# try:
#     print("Fetching data...")
#     data = requests.get(URI)

#     if data.status_code == 200:
#         response = data.json()

#         # Collect only completed todos
#         final_todos = [todo for todo in response if todo["completed"]]

#         print(f"Found {len(final_todos)} completed todos.")
#         print("Saving to file...")

#         # Save filtered todos to a file
#         with open("todos.json", "w") as file:
#             json.dump(final_todos, file, indent=4)

#         print("Data saved to file.")
#     else:
#         print("Failed with status:", data.status_code)

# except Exception as e:
#     print("Data fetch failed:", e)


# ------------------ Working with CSV Files ------------------ #

# import csv

# # Ask user for a city to search
# city_to_find = input("Enter your city: ")

# # Sample contact data
# contacts = [
#     {"name": "Alice", "phone": "1234567890", "city": "New York"},
#     {"name": "Bob", "phone": "9876543210", "city": "London"},
#     {"name": "Sara", "phone": "5556667777", "city": "New York"},
# ]

# # Write contacts to CSV file
# with open("contacts.csv", 'w', newline='') as file:
#     field_names = ["name", "phone", "city"]
#     writer = csv.DictWriter(file, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(contacts)

# # Search CSV for matching city
# with open("contacts.csv", 'r') as file:
#     reader = csv.DictReader(file)
#     found = False

#     for row in reader:
#         if row["city"].lower() == city_to_find.lower():
#             print(f"Name: {row['name']}, Phone: {row['phone']}")
#             found = True

#     if not found:
#         print("No matches found for this city name!")


# ------------------ CSV: Calculate Averages & Save ------------------ #

# import csv

# # Step 1: Define student data (without averages)
# students = [
#     {"name": "Alice", "math": "85", "science": "90", "english": "88"},
#     {"name": "Bob", "math": "78", "science": "82", "english": "85"},
#     {"name": "Sara", "math": "92", "science": "88", "english": "95"},
# ]

# # Step 2: Write original student data to CSV (with average column added, but empty)
# with open("students.csv", "w", newline="") as file:
#     field_names = ["name", "math", "science", "english", "average"]
#     writer = csv.DictWriter(file, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(students)  # currently no averages included

# # Step 3: Read from CSV, calculate average, track top student
# updated_students = []  # to store updated rows with averages
# highest_average = 0
# top_student = ""

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Convert string marks to integers
#         math = int(row["math"])
#         science = int(row["science"])
#         english = int(row["english"])

#         # Calculate average
#         average = (math + science + english) / 3
#         row["average"] = f"{average:.2f}"  # format to 2 decimal places

#         # Track highest average and top student
#         if average > highest_average:
#             highest_average = average
#             top_student = row["name"]

#         updated_students.append(row)  # store updated row

# # Step 4: Show top student
# print(f"\nTop student is {top_student} with an average of {highest_average:.2f}")

# # Step 5: Write updated student data (with averages) to new CSV file
# with open("students_with_avg.csv", "w", newline="") as file:
#     field_names = ["name", "math", "science", "english", "average"]
#     writer = csv.DictWriter(file, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(updated_students)


