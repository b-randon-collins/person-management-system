import os
from navigation_options.update_person_options import update_person_options
from navigation_options.delete_person_options import delete_person_options

def view_person_options(selected_person):
    os.system('clear')

    print("\n===View Person Details===")
    print(f"Name: {selected_person.name}")
    print(f"DOB: {selected_person.dob}")
    
    print("\nPhone Numbers:")
    print("Not implemented")
    
    print("\nEmail Addresses:")
    print("Not implemented")

    print("\n===Actions===")
    print("1. Update Person")
    print("2. Delete Person")
    print("3. Return to Main Menu")

    choice = input("\nSelect an option: ")

    if choice == '1':
        update_person_options(selected_person)
    elif choice == '2':
        delete_person_options(selected_person)
    elif choice == '3':
        return
    else:
        print("Error: Invalid option selected.")
