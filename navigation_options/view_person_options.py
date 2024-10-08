import os
from navigation_options.update_person_options import update_person_options
from navigation_options.delete_person_options import delete_person_options

def view_person_options(selected_person):
    os.system('clear')

    print("\nPerson\n")
    print(f"{selected_person.name}")
    print(f"DOB: {selected_person.dob}")
    
    print("\nPhone Numbers:")
    print("Not implemented")
    
    print("\nEmail Addresses:")
    print("Not implemented")

    print("\n1. Update Person")
    print("2. Delete Person")
    print("3. Return to Main Menu")

    choice = input("\n> ")

    if choice == '1':
        update_person_options(selected_person)
    elif choice == '2':
        result = delete_person_options(selected_person)
        if result == "deleted":
            os.system('clear')
            return
    elif choice == '3':
        return
    else:
        print("Error: Invalid option selected.")
