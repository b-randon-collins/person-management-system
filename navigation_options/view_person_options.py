import os
from db import initialize_database

def view_person_options(selected_person):
    os.system('clear')

    print("\n===View Person Details===")
    
    print(f"Name: {selected_person.name}")
    print(f"DOB: {selected_person.dob}")
    
    print("\nPhone Numbers:")
    print("Not implemented")
    
    print("\nEmail Addresses:")
    print("Not implemented")
