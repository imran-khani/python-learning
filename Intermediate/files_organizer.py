import os
import shutil

# Folder to organize (current folder here)
folder_path = "."

# All files in the folder
files = os.listdir(folder_path)
print("Files found:", files)

# File types dictionary
file_types = {
    "Music": ["mp3", "wav"],
    "Videos": ["mp4", "mkv"],
    "Pictures": ["jpg", "png"],
    "Documents": ["pdf", "docx", "txt"]
}

# Loop through files
for file in files:
    # Skip folders
    if os.path.isdir(os.path.join(folder_path, file)):
        continue

    # Get file extension
    ext = file.split(".")[-1].lower()

    # Match file with category
    for folder, extensions in file_types.items():
        if ext in extensions:
            folder_name = os.path.join(folder_path, folder)

            # Create folder if it doesn’t exist
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            # Move the file
            shutil.move(os.path.join(folder_path, file), folder_name)
            print(f"Moved {file} to {folder}/")
            break
