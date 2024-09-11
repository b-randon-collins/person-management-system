def delete_person_options(selected_person):
    confirmation = input(f"Are you sure you want to delete {selected_person.name}? (y/n): ")

    if confirmation.lower() == 'y':
        # Here, delete the person from the database
        print(f"{selected_person.name} has been deleted.")
    else:
        print("Delete operation cancelled.")
