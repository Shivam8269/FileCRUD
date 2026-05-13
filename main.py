# Project - CRUD opration

from pathlib import Path
import os       # oprating system   --> use to delete the file 

def readfileandfolder():
    try:
        p = Path('')
        item = list(p.rglob('*'))               # p.rglob take all the files from this folder
        for index , file in enumerate(item):
            print(f'{index+1} - {file}')
    except Exception as e:
        print(e)



def create_file():
    try:
        readfileandfolder()
        # d:/CODE/Python/file_handling/hello.txt
        file_name = input("Enter name of your file: ")
        p = Path(file_name)
        if p.exists():
            print("FILE ALREADY EXIST")
        else:
            with open(file_name,'w') as file:
                content = input("Enter your file contenet: ")
                file.write(content)
                print('FILE ADDED!')
            print("FILE CREATED SUCESSFULLY")
    except Exception as e:
        print(e)
def read_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file:")
        p = Path(file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print("FILE NOT FOUND! ")
    except Exception as e:
        print(e)

def update_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file:")
        p = Path(file_name)
        if p.exists():
            print('Press 1 to overwrite the content')
            print('print 2 to append new content')
            option = int(input("Enter ypur choice for updating flie: "))
            if option == 1:
                with open(file_name,'a') as file:
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED...')

            elif option == 2:
                with open(file_name,'a') as file:
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED...')
            else:
                print("INVALID INPUT!")
        else:
            print('FLIE DOES NOT EXISTS!')
    except Exception as e:
        print(e)

def delete_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file:")
        p = Path(file_name)
        if p.exists():
            os.remove(p)                #--> OS is removing path of that file completely from the system.
            print( "FILE DELETED")
    except Exception as e:
        print(e)
            
def rename_file():
    readfileandfolder()
    file_name = input('Enter name of your file: ')
    p = Path(file_name)
    if p.exists():
        new_file = input('Enter new name of your file: ')
        p.rename(new_file)
        print('FILE RENAMED!')
    else:
        print('FILE NOT FOUND!') 

def create_folder():
    readfileandfolder()
    folder_name = input('Enter name of your folder: ')
    p = Path(folder_name)
    if p.exists():
        print('FOLDER ALREADY CREATED!')
    else:
        p.mkdir()               # do not need to add name of folder in bracket()
        print('FOLDER CREATED!')


def remove_folder():
    readfileandfolder()
    folder_name = input('Enter the name of folder you want to remove: ')
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print('FOLDER REMOVED!')
    else:
        print('FOLDER NOT FOUND!')


def create_file_in_folder():
    folder_name = input("Enter name of your folder: ")
    file_name = input("Enter name of tour file: ")
    p = Path(folder_name/file_name)
    if p.exists():
        print('FILE ALREADY EXIST!')
    else:
        pass




while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("print 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 for rename a file")
    print("Press 6 for creating a folder")
    print("Press 7 for removing a folder")
    print("Press 0 for exiting...")

    option = int(input("Enter your choice: "))

    if option == 1:
        create_file()

    if option == 2:
        read_file()

    if option == 3:
        update_file()

    if option == 4:
        delete_file()

    if option == 5:
        rename_file()

    if option == 6:
        create_folder()

    if option == 7:
        remove_folder()

    if option == 0:
        break







