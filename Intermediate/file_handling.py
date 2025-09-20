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

import requests
import json


URI = 'https://jsonplaceholder.typicode.com/todos'





