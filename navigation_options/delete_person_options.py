import time

def delete_person_options(selected_person):
    confirmation = input(f"Are you sure you want to delete {selected_person.name}? (y/n): ")

    if confirmation.lower() == 'y':
        try:
            print(f"{selected_person.name} has been deleted.")
        except Exception as e:
            print(f"Error deleting person: {str(e)}")
        time.sleep(1)
    else:
        print("Delete operation cancelled.")
        time.sleep(1)
        return "cancelled"
