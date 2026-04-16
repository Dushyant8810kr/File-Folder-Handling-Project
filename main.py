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
        name = input("Enter your Folder name : ")                       # taking the name as input from user for creatinga folder
        p = Path(name)                                                  # copy the path of inputed name    
        p.mkdir()                                                       # making the directiory for inputed name path
        print("Folder is successfully created.")                        # simmply prints the message after succesful creation of folder
    except Exception as err:                                            # if there is any issue in folder creation then this will handle this.
        print("Your folder is already exist!!")                         # simply prints taht your file is already exist.

def read_folder():
    p = Path("")
    count = 1                                                           # for indexing purpose for folder or file
    for item in os.listdir(p) :                                         # os.listdir(p) ->get all files/folders
        if item.startswith("."):                                        #skip hiddenFiles like .git , .vscode  etc
            continue
        print(f"{count}",item)                                          # print the file/folder with count
        count+=1
        
def update_folder():
    try:
        read_folder()                                                           # providing the files and folders name
        name = input("Enter your folder name that you want to update : ")       # taking folder name input from user for rename the preexisting file
        p = Path(name)                                                          # store path of it in a variable 
        if p.exists() and p.is_dir():                                           # checking the condition tat the inputed folder name is exist or not
            new_name = input("Enter new name of the folder : ")                 # taking folder new name as input from user
            p.rename(new_name)                                                  # changing the folder/file name
            print(f"Your folder succesfully update to {new_name}")              
        else:
            print("Your folder does not exist")
    except Exception as err:
        print(f"showing error as {err}")

def delete_folder():
    try:
        read_folder()
        name = input("Enter the name of folder that you want to delete : ")
        p = Path(name)
        if p.exists() and p.is_dir():
            p.rmdir()
            print("Your file succesfully deleted.")
        else:
            print("your file doesnot exist!!")
    except Exception as err:
        print(f"Showing error as {err}")



if option==1:
    create_folder()

if option==2:
    read_folder()

if option==3:
    update_folder()

if option ==4:
    delete_folder()




