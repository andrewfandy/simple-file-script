import os
import sys
import shutil
import re

# Get the current directory where the script is located
curr_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


# Define a helper function to extract the numeric part of the filenames
def extract_number(filename):
    match = re.search(r"(\d+)", filename)
    return int(match.group(0)) if match else 0


inp = input("Choose Y to start: ").lower()
if inp == "y":
    # Define the directory where old files are stored
    old_files_dir = os.path.join(curr_dir, "old_files")
    if not os.path.exists(old_files_dir):
        os.makedirs(old_files_dir)
    old_files = sorted(os.listdir(old_files_dir), key=extract_number)

    # Define the starting name for renaming
    starting_name = int(input("Input starting number: "))

    # Create the new files directory if it doesn't exist
    new_files_dir = os.path.join(curr_dir, "new_files")
    if not os.path.exists(new_files_dir):
        os.makedirs(new_files_dir)

    ls = []

    # Rename and move files from old_files to new_files
    for i in range(len(old_files)):
        ext = ".png"
        old_file_name = old_files[i]
        new_file_name = str(starting_name) + ext
        old_file_path = os.path.join(old_files_dir, old_file_name)
        new_file_path = os.path.join(new_files_dir, new_file_name)

        # Check if the old file exists before moving
        if old_file_name in old_files:
            shutil.move(old_file_path, new_file_path)
            print(f"Moving {old_file_name} to {new_file_name} - Success")
            starting_name += 1  # Increment the starting name for the next file
        else:
            print(f"{old_file_name} not found in {old_files_dir}")
else:
    print("Goodbye")
