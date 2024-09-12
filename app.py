import os
import time
import sqlite3
import re
from datetime import datetime
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_dob(dob):
    try:
        datetime.strptime(dob, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def main_menu():
    clear_screen()
    print("\nMain Menu:\n")
    print("1. Add Person")
    print("2. List People")
    print("3. Exit")

    while True:
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

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None

PHONE_NUMBER_PATTERNS = [
    r'^\d{7}$',                # xxxxxxx
    r'^\d{11}$',               # xxxxxxxxxxx
    r'^\d{3}-\d{3}-\d{4}$',    # xxx-xxx-xxxx
    r'^\d{3}-\d{3}-\d{4}$',  # xxx-xxx-xxxx
    r'^\d{1}-\d{3}-\d{3}-\d{4}$'  # x-xxx-xxx-xxxx
]

def is_valid_phone_number(phone_number):
    for pattern in PHONE_NUMBER_PATTERNS:
        if re.fullmatch(pattern, phone_number):
            return True
    return False

def add_person_workflow():
    clear_screen()
    print("\nAdd a new person:\n")

    name = input("Enter the person's name (required): ").strip()

    if not name:
        print("Name cannot be empty.")
        retry = input("Do you want to try again? (y/n): ").lower()
        if retry == 'y':
            add_person_workflow()
        else:
            print("Returning to the main menu...")
            time.sleep(1)
            main_menu()
        return

  
    dob = input("Enter the person's DOB (optional, format: MM/DD/YYYY): ")
    if dob and not validate_dob(dob):
        print("Invalid date format. Please use MM/DD/YYYY.")
        time.sleep(1)
        add_person_workflow()
        return

  
    person_id = Person.add_person(name, dob)
    print(f"\nPerson '{name}' added successfully.")
    time.sleep(1)

  
    next_step_menu(person_id)

def next_step_menu(person_id):
    """Displays the next steps after adding a person."""
    print("\nWhat would you like to do next?")
    print("1. View the entry")
    print("2. Create a new person")
    print("3. Return to main menu")

    while True:
        choice = input("\n > ")
        if choice == '1':
            view_person_workflow(person_id)
            break
        elif choice == '2':
            add_person_workflow()
            break
        elif choice == '3':
            main_menu()
            break
        else:
            print("Invalid choice! Please try again.")

def list_people_workflow():
    clear_screen()
    people = Person.list_people()

    if not people:
        print("\nNo people found.\n")
        print("1. Add a new person")
        print("2. Return to main menu")
        choice = input("\n > ")

        if choice == '1':
            add_person_workflow()
        elif choice == '2':
            main_menu()
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
            list_people_workflow()
        return

    for i, person in enumerate(people, start=1):
        print(f"{i}. {person.name}")

    try:
        person_index = int(input("Select person by number to view details: ")) - 1
        if 0 <= person_index < len(people):
            view_person_workflow(people[person_index].id)
        else:
            print("Invalid number! Please try again.")
            time.sleep(1)
            list_people_workflow()
    except ValueError:
        print("Invalid input! Please enter a number.")
        time.sleep(1)
        list_people_workflow()
    clear_screen()
    people = Person.list_people()

    if not people:
        print("\nNo people found.\n")
        print("1. Add a new person")
        print("2. Return to main menu")
        choice = input("\n > ")

        if choice == '1':
            add_person_workflow()
        elif choice == '2':
            main_menu()
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
            list_people_workflow()
        return

    for i, person in enumerate(people, start=1):
        print(f"{i}. {person.name}")

    try:
        person_id = int(input("Select person by ID to view details: "))
        if 1 <= person_id <= len(people):
            view_person_workflow(person_id)
        else:
            print("Invalid ID! Please try again.")
            time.sleep(1)
            list_people_workflow()
    except ValueError:
        print("Invalid input! Please enter a number.")
        time.sleep(1)
        list_people_workflow()

def view_person_workflow(person_id):
    clear_screen()
    person = Person.get_person(person_id)
    
    if person:
        print(f"Name: {person.name}")
        print(f"DOB: {person.dob}\n")

        phone_numbers = PhoneNumber.get_phone_numbers(person_id)
        print("Phone numbers:")
        for phone in phone_numbers:
            print(f"  {phone[2]}")  

        email_addresses = EmailAddress.get_email_addresses(person_id)
        print("Email addresses:\n")
        for email in email_addresses:
            print(f"  {email[2]}")  
            print("")  

        view_person_options(person_id)
    else:
        print("Person not found.")
        time.sleep(1)
        list_people_workflow()

def view_person_options(person_id):
    print("1. Update person")
    print("2. Delete person")
    print("3. Return to list")
    print("4. Return to Main Menu")

    while True:
        choice = input("\n > ")
        if choice == '1':
            update_person_options(person_id)
        elif choice == '2':
            if input("Are you sure? (y/n): ").lower() == 'y':
                Person.delete_person(person_id)
                print("Person deleted.")
                time.sleep(1)
                list_people_workflow()
                return
            else:
                view_person_workflow(person_id)
        elif choice == '3':
            list_people_workflow()
            return
        elif choice == '4':
            main_menu()
            return
        else:
            print("Invalid choice! Please try again.")

def update_person_workflow(person_id):
    clear_screen()
    person = Person.get_person(person_id)
    if person:
        print("")

        print(f"Name: {person.name}")
        print(f"DOB: {person.dob}\n")

        phone_numbers = PhoneNumber.get_phone_numbers(person_id)
        print("Phone numbers:")
        for phone in phone_numbers:
            print(f"  {phone[2]}")  

        email_addresses = EmailAddress.get_email_addresses(person_id)
        print("Email addresses:\n")
        for email in email_addresses:
            print(f"  {email[2]}")  

        view_person_workflow(person_id)
    else:
        print("Person not found.")
        time.sleep(1)
        list_people_workflow()

def update_name(person_id):
    while True:
        new_name = input("Enter the new name: ").strip()
        if not new_name:
            print("Name cannot be empty. Please enter a valid name.")
            retry = input("Do you want to try again? (y/n): ").lower()
            if retry != 'y':
                print("Returning to the update options...")
                time.sleep(1)
                return
        else:
            person = Person.get_person(person_id)
            if person.name != new_name:
                Person.edit_name(person_id, new_name)
                print("Name changed successfully.")
            else:
                print("Name unchanged.")
            time.sleep(1)
            return

def update_person_options(person_id, auto_select=None):
    clear_screen()
    person = Person.get_person(person_id)
    if not person:
        print("Person not found.")
        return

    print(f"Name: {person.name}")
    print(f"DOB: {person.dob}\n")

    phone_numbers = PhoneNumber.get_phone_numbers(person_id)
    email_addresses = EmailAddress.get_email_addresses(person_id)

    print("Phone numbers:")
    for i, phone in enumerate(phone_numbers):
        print(f"  {i + 1}. {phone[2]}")

    print("")

    print("Email addresses:")
    for i, email in enumerate(email_addresses):
        print(f"  {i + 1}. {email[2]}")

    if auto_select is None:
        auto_select = []

    print("\n1. Edit name")
    print("2. Edit DOB")
    print("3. Update phone numbers")
    print("4. Update email addresses")
    print("5. Back")

    choice = auto_select.pop(0) if auto_select else input("\n > ")

    if choice == '1':
        update_name(person_id)
    elif choice == '2':
        new_dob = input("Enter the new DOB (format: MM/DD/YYYY): ")
        if not validate_dob(new_dob):
            print("Invalid date format. Please use MM/DD/YYYY.")
            if input("Do you want to retry? (y/n): ").lower() == 'y':
                new_dob = input("Enter the new DOB (format: MM/DD/YYYY): ")
        if person.dob != new_dob:
            Person.edit_dob(person_id, new_dob)
            print("DOB changed successfully.")
        else:
            print("DOB unchanged.")
    elif choice == '3':
        update_phone_numbers_options(person_id, auto_select)
    elif choice == '4':
        update_email_addresses_options(person_id, auto_select)
    elif choice == '5':
        view_person_workflow(person_id)
        return
    else:
        print("Invalid choice! Please try again.")

    time.sleep(1)
    update_person_options(person_id, auto_select)
    clear_screen()
    person = Person.get_person(person_id)
    if not person:
        print("Person not found.")
        return
    
    print(f"Name: {person.name}")
    print(f"DOB: {person.dob}\n")

    phone_numbers = PhoneNumber.get_phone_numbers(person_id)
    email_addresses = EmailAddress.get_email_addresses(person_id)

    print("Phone numbers:")
    for i, phone in enumerate(phone_numbers):
        print(f"  {i + 1}. {phone[2]}")  

        
    print("")
    print("Email addresses:")
    print("")

    for i, email in enumerate(email_addresses):
        print(f"  {i + 1}. {email[2]}") 

    if auto_select is None:
        auto_select = []

    print("\n1. Edit name")
    print("2. Edit DOB")
    print("3. Update phone numbers")
    print("4. Update email addresses")
    print("5. Back")

    choice = auto_select.pop(0) if auto_select else input("\n > ")

    if choice == '1':
        update_name(person_id)
    elif choice == '2':
        new_dob = input("Enter the new DOB (format: MM/DD/YYYY): ")
        if new_dob and not validate_dob(new_dob):
            print("Invalid date format. Please use MM/DD/YYYY.")
            new_dob = input("Enter the new DOB (format: MM/DD/YYYY): ")
        if person.dob != new_dob:
            Person.edit_dob(person_id, new_dob)
            print("DOB changed successfully.")
        else:
            print("DOB unchanged.")
    elif choice == '3':
        update_phone_numbers_options(person_id, auto_select)
    elif choice == '4':
        update_email_addresses_options(person_id, auto_select)
    elif choice == '5':
        view_person_workflow(person_id)
        return
    else:
        print("Invalid choice! Please try again.")
    
    time.sleep(1)
    update_person_options(person_id, auto_select)
    while True:
        clear_screen()
        person = Person.get_person(person_id)
        if not person:
            print("Person not found.")
            return
        
        print(f"Name: {person.name}")
        print(f"DOB: {person.dob} \n")

        phone_numbers = PhoneNumber.get_phone_numbers(person_id)
        print("Phone numbers:")
        for phone in phone_numbers:
            print(f"  {phone[2]}")  

        email_addresses = EmailAddress.get_email_addresses(person_id)
        print("Email addresses:")
        for email in email_addresses:
            print(f"  {email[2]}") 
        print("")

        print("1. Edit name")
        print("2. Edit DOB")
        print("3. Update phone numbers")
        print("4. Update email addresses")
        print("5. Back")

        choice = str(auto_select) if auto_select is not None else input("\n > ")

        if choice == '1':
            update_name(person_id)
        elif choice == '2':
            new_dob = input("Enter the new DOB (format: MM/DD/YYYY): ")
            if new_dob and not validate_dob(new_dob):
                print("Invalid date format. Please use MM/DD/YYYY.")
                new_dob = input("Enter the new DOB (format: MM/DD/YYYY): ")
            if person.dob != new_dob:
                Person.edit_dob(person_id, new_dob)
                print("DOB changed successfully.")
            else:
                print("DOB unchanged.")
            time.sleep(1)
        elif choice == '3':
            update_phone_numbers_options(person_id)
        elif choice == '4':
            update_email_addresses_options(person_id)
        elif choice == '5':
            view_person_workflow(person_id)
            return
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
            update_person_options(person_id, auto_select=None)

def update_phone_numbers_options(person_id, auto_select=None):
    def display_options():
        clear_screen()
        person = Person.get_person(person_id)
        if not person:
            print("Person not found.")
            return

        print(f"Name: {person.name}")
        print(f"DOB: {person.dob}\n")

        phone_numbers = PhoneNumber.get_phone_numbers(person_id)
        print("Phone numbers:")
        for i, phone in enumerate(phone_numbers):
            print(f"{i + 1}. {phone[2]}")

        print("\n1. Add phone number")
        print("2. Update phone numbers")
        print("3. Back")

        return phone_numbers

    while True:
        phone_numbers = display_options()
        if phone_numbers is None:
            return

        if auto_select is None:
            auto_select = []

        choice = auto_select.pop(0) if auto_select else input("\n > ")

        if choice == '1':
            while True:
                phone_number = input("Phone Number xxx-xxx-xxxx: ").strip()
                if is_valid_phone_number(phone_number):
                    PhoneNumber.add_phone_number(person_id, phone_number)
                    print("Phone number added successfully.")
                    if input("Add another? (y/n): ").lower() != 'y':
                        break
                else:
                    print("Invalid phone number format. Please try again.")
                    if input("Do you want to retry? (y/n): ").lower() != 'y':
                        break
        elif choice == '2':
            if not phone_numbers:
                print("No phone numbers to update.")
                time.sleep(1)
                continue

            while True:
                try:
                    phone_id = int(input("Select phone number by ID to update: ")) - 1
                    if 0 <= phone_id < len(phone_numbers):
                        while True:
                            new_phone_number = input("Enter the new phone number: ").strip()
                            if is_valid_phone_number(new_phone_number):
                                PhoneNumber.edit_phone_number(phone_numbers[phone_id][0], new_phone_number)
                                print("Phone number updated successfully.")
                                time.sleep(1)
                                break
                            else:
                                print("Invalid phone number format. Please try again.")
                                if input("Do you want to retry? (y/n): ").lower() != 'y':
                                    break
                        break
                    else:
                        print("Invalid ID! Please try again.")
                        if input("Do you want to retry? (y/n): ").lower() != 'y':
                            break
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    if input("Do you want to retry? (y/n): ").lower() != 'y':
                        break
        elif choice == '3':
            return
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)

def update_email_addresses_options(person_id, auto_select=None):
    clear_screen()
    person = Person.get_person(person_id)
    if not person:
        print("Person not found.")
        return

    print(f"Name: {person.name}")

    email_addresses = EmailAddress.get_email_addresses(person_id)
    if email_addresses:
        print("Email addresses:")
        for i, email in enumerate(email_addresses):
            print(f"{i + 1}. {email[2]}")
    else:
        print("No email addresses to update.")

    if auto_select is None:
        auto_select = []

    print("\n1. Add email address")
    print("2. Update email addresses")
    print("3. Back")

    choice = auto_select.pop(0) if auto_select else input("\n > ")

    if choice == '1':
        while True:
            email_address = input("Email Address (email@domain.com): ").strip()
            if is_valid_email(email_address):
                EmailAddress.add_email_address(person_id, email_address)
                print("Email address added successfully.")
                if input("Add another? (y/n): ").lower() != 'y':
                    break
            else:
                print("Invalid email address format. Please try again.")
                if input("Do you want to retry? (y/n): ").lower() != 'y':
                    break
    elif choice == '2':
        if not email_addresses:
            print("No email addresses to update.")
            time.sleep(1)
            return

        while True:
            try:
                email_id = int(input("Select email address by ID to update: ")) - 1
                if 0 <= email_id < len(email_addresses):
                    while True:
                        new_email_address = input("Enter the new email address: ").strip()
                        if is_valid_email(new_email_address):
                            EmailAddress.edit_email_address(email_addresses[email_id][0], new_email_address)
                            print("Email address updated successfully.")
                            time.sleep(1)
                            break
                        else:
                            print("Invalid email address format. Please try again.")
                            if input("Do you want to retry? (y/n): ").lower() != 'y':
                                break
                    break
                else:
                    print("Invalid ID! Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    elif choice == '3':
        return
    else:
        print("Invalid choice! Please try again.")
    
    time.sleep(1)
    update_email_addresses_options(person_id, auto_select)
    clear_screen()
    person = Person.get_person(person_id)
    if not person:
        print("Person not found.")
        return

    print(f"Name: {person.name}")

    email_addresses = EmailAddress.get_email_addresses(person_id)
    if email_addresses:
        print("Email addresses:")
        for i, email in enumerate(email_addresses):
            print(f"{i + 1}. {email[2]}")  
    else:
        print("No email addresses to update.")

    if auto_select is None:
        auto_select = []

    print("\n1. Add email address")
    print("2. Update email addresses")
    print("3. Back")

    choice = auto_select.pop(0) if auto_select else input("\n > ")

    if choice == '1':
        while True:
            email_address = input("Email Address: ").strip()
            if is_valid_email(email_address):
                EmailAddress.add_email_address(person_id, email_address)
                print("Email address added successfully.")
                if input("Add another? (y/n): ").lower() != 'y':
                    break
            else:
                print("Invalid email address format. Please try again.")
                if input("Do you want to try again? (y/n): ").lower() != 'y':
                    break
    elif choice == '2':
        if not email_addresses:
            print("No email addresses to update.")
            time.sleep(1)
            return

        while True:
            try:
                email_id = int(input("Select email address by ID to update: ")) - 1
                if 0 <= email_id < len(email_addresses):
                    while True:
                        new_email_address = input("Enter the new email address: ").strip()
                        if is_valid_email(new_email_address):
                            EmailAddress.edit_email_address(email_addresses[email_id][0], new_email_address)
                            print("Email address updated successfully.")
                            time.sleep(1)
                            break
                        else:
                            print("Invalid email address format. Please try again.")
                            if input("Do you want to try again? (y/n): ").lower() != 'y':
                                break
                    break
                else:
                    print("Invalid ID! Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    elif choice == '3':
        return
    else:
        print("Invalid choice! Please try again.")
    
    time.sleep(1)
    update_email_addresses_options(person_id, auto_select)
    clear_screen()
    person = Person.get_person(person_id)
    if not person:
        print("Person not found.")
        return

    print(f"Name: {person.name}")

    email_addresses = EmailAddress.get_email_addresses(person_id)
    if email_addresses:
        print("\nEmail addresses:")
        for i, email in enumerate(email_addresses):
            print(f"{i + 1}. {email[2]}")  
    else:
        print("No email addresses to update.")

    print("\n1. Add email address")
    print("2. Update email addresses")
    print("3. Back")

    while True:
        choice = input("\n > ")

        if choice == '1':
            while True:
                email_address = input("Email Address: ").strip()
                if is_valid_email(email_address):
                    EmailAddress.add_email_address(person_id, email_address)
                    print("Email address added successfully.")
                    if input("Add another? (y/n): ").lower() != 'y':
                        break
                else:
                    print("Invalid email address format. Please try again.")
                    if input("Do you want to try again? (y/n): ").lower() != 'y':
                        break
            return

        elif choice == '2':
            if not email_addresses:
                print("No email addresses to update.")
                time.sleep(1)
                return

            for i, email in enumerate(email_addresses):
                print(f"{i + 1}. {email[2]}")  
            
            while True:
                try:
                    email_id = int(input("Select email address by ID to update: ")) - 1
                    if 0 <= email_id < len(email_addresses):
                        while True:
                            new_email_address = input("Enter the new email address: ").strip()
                            if is_valid_email(new_email_address):
                                EmailAddress.edit_email_address(email_addresses[email_id][0], new_email_address)
                                print("Email address updated successfully.")
                                time.sleep(1)
                                break
                            else:
                                print("Invalid email address format. Please try again.")
                                if input("Do you want to try again? (y/n): ").lower() != 'y':
                                    break
                        break
                    else:
                        print("Invalid ID! Please try again.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue
            return

        elif choice == '3':
            return

        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)

if __name__ == '__main__':
    initialize_db()
    main_menu()
