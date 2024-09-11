# main_menu.py
import os
from person import Person
from db import initialize_database
from navigation_options.list_person_options import list_person_options

def main_menu():
    initialize_database()
    os.system('clear')

    while True:
        print("\n===Main Menu===")
        print("1. Add person")
        print("2. List people")
        print("3. Exit")
        choice = input("\nSelect an option: ")

        if choice == '1':
            print("\n1: Add person")
            Person.add_person()

        elif choice == '2':
            people_list = Person.list_people()
            if not people_list:
                print("No people found in the database.")
            else:
                list_person_options(people_list)
        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Error: Invalid choice. Please select a valid option.")
