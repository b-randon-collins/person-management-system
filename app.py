import sqlite3
import time
from classes.person import Person
from classes.phone_number import PhoneNumber
from classes.email_address import EmailAddress

def initialize_db():
    conn = sqlite3.connect('resource.db')
    Person.create_table()
    PhoneNumber.create_table()
    EmailAddress.create_table()
    conn.commit()
    conn.close()

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Add Person")
        print("2. List People")
        print("3. Exit")
        
        choice = input("> Select an option: ")
        if choice == '1':
            add_person_workflow()
        elif choice == '2':
            break
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice! Please try again.")

def add_person_workflow():
    name = input("Enter the person's name: ")
    dob = input("Enter the person's DOB (optional): ")

    person_id = Person.add_person(name, dob) 

    print(f"\nPerson '{name}' added successfully with ID {person_id}!")

    while True:
        print("\nWhat would you like to do next?")
        print("1. View the entry")
        print("2. Create a new person")
        print("3. Return to main menu")
        choice = input("> Select an option: ")

        if choice == '1':
             break
        elif choice == '2':
            return
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    initialize_db()
    main_menu()
