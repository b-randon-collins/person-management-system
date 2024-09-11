def update_person_options(selected_person):
    print("\n===Update Person Options===")
    
    # Display the current person details
    print(f"Current Name: {selected_person.name}")
    new_name = input("Enter new name (leave blank to keep the same): ")

    if new_name:
        selected_person.name = new_name

    # You can add more fields (e.g., DOB, phone number, email) similarly
    print(f"Person {selected_person.name} updated successfully.")
