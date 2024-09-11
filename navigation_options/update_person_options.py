import os
import time
from navigation_options.update_phone_numbers_options import update_phone_numbers_options
from navigation_options.update_email_addresses_options import update_email_addresses_options

def update_person_options(selected_person):
    os.system('clear')

    while True:
        os.system('clear')

        print("\nUpdate Person\n")
        print(f"1. Edit Name (current: {selected_person.name})")
        print(f"2. Edit Birthday (current: {selected_person.dob})")
        print("3. Update Phone Numbers")
        print("4. Update Email Addresses")
        print("5. Return to View Person Options")

        choice = input("\n> ")

        if choice == '1':
            new_name = input("Enter new name (leave blank to keep the same): ")
            if new_name:
                selected_person.name = new_name
                print(f"Name updated to {selected_person.name}")
            else:
                print("Name unchanged.")
            time.sleep(2) 

        elif choice == '2':
            new_dob = input(f"Enter new DOB (leave blank to keep the same): ")
            if new_dob:
                selected_person.dob = new_dob
                print(f"DOB updated to {selected_person.dob}")
            else:
                print("DOB unchanged.")
            time.sleep(1)
        
        elif choice == '3':
            update_phone_numbers_options(selected_person)

        elif choice == '4':
            update_email_addresses_options(selected_person)
        
        elif choice == '5':
            break

        else:
            print("Invalid option. Please select again.")
            time.sleep(2)  # Pause for 2 seconds if an invalid option is selected
