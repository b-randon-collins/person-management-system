import sqlite3
import time
import os
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
    os.system('clear')
    while True:
        print("")
        print("Main Menu:")
        print("1. Add Person")
        print("2. List People")
        print("3. Exit")
        
        choice = input("\n > ")
        if choice == '1':
            add_person_workflow()
        elif choice == '2':
            list_people_workflow()
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
        choice = input("\n > ")

        if choice == '1':
            break
        elif choice == '2':
            add_person_workflow()
            return
        elif choice == '3':
            return
        else:
            print("Invalid choice! Please try again.")

def list_people_workflow():
    os.system('clear')
    people = Person.list_people()
    for i, person in enumerate(people, start=1):
        print(f"{i}. {person.name}")

    person_id = int(input("\n > "))
    view_person_workflow(person_id)

def view_person_workflow(person_id):
    os.system('clear')
    person = Person.get_person(person_id)
    
    if person:
        print(f"Name: {person.name}")
        print(f"DOB: {person.dob}")

        phone_numbers = PhoneNumber.get_phone_numbers(person_id)
        print("Phone numbers:")
        for phone in phone_numbers:
            print(f"  {phone[2]}")  

        email_addresses = EmailAddress.get_email_addresses(person_id)
        print("Email addresses:")
        for email in email_addresses:
            print(f"  {email[2]}")  

        return
    else:
        print("Person not found.")
        time.sleep(1)
        list_people_workflow()




if __name__ == "__main__":
    initialize_db()
    main_menu()
