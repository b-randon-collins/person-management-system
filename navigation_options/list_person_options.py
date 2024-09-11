import os
from navigation_options.view_person_options import view_person_options

def list_person_options(people_list):
    
    choices = {}

    os.system('clear')

    while True:
        print("\nPeople\n")
        
        for person in people_list:
            print(f"{person.id}. {person.name}")
            choices[person.id] = person
            
        choice = input("\n> ")
        
        if choice.isdigit() and int(choice) in choices:
            selected_person = choices[int(choice)]
            print(f"\nSelected person: {selected_person.name}")
            
            view_person_options(selected_person)
            break
            
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Error: Invalid choice. Please select a valid option.")
