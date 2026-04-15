from pathlib import Path
import os

print("Options : ")
print("1. Create a folder.")
print("2. Read files and folders.")
print("3. Update the folder.")
print("4. Delte te folder.")

option = int(input("Choose an option : "))


def create_folder():
    try:
        name = input("Enter your file name : ")
        p = Path(name)
        p.mkdir()
        print("Folder is successfully created.")
    except Exception as err:
        print("Your folder is already exist!!")
    


if option==1:
    create_folder()
