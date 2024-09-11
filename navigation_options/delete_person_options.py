import time
def delete_person_options(selected_person):
    confirmation = input(f"Are you sure you want to delete {selected_person.name}? (y/n): ")

    if confirmation.lower() == 'y':
        print(f"{selected_person.name} has been deleted.")
        time.sleep(2)
    else:
        print("Delete operation cancelled.")
