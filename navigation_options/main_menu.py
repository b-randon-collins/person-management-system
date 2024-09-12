# main_menu.py
import os
import time
from person import Person
from navigation_options.list_person_options import list_person_options
from initialize import initialize_database

def main_menu():
    os.system('clear')

    while True:
        os.system('clear')
        print("\nMain Menu\n")
        print("1. Add person")
        print("2. List people")
        print("3. Exit")
        choice = input("\n> ")

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
            time.sleep(1)
