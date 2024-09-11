import os

def update_phone_numbers_options(selected_person):
    os.system('clear')

    while True:
        print("\nUpdate Phone Numbers")
        print("1. Add Phone Number")
        print("2. Update Existing Phone Numbers")
        print("3. Return to Update Person Options")

        choice = input("\n> ")

        if choice == '1':
            while True:
                phone_number = input("Enter Phone Number (7 or 10 digits): ")
                if len(phone_number) in [7, 10] and phone_number.isdigit():
                    selected_person.phone_numbers.append(phone_number)
                    print(f"Phone number {phone_number} added.")
                    add_more = input("Add another? (y/n): ")
                    if add_more.lower() != 'y':
                        break
                else:
                    print("Invalid phone number format. Please try again.")

        elif choice == '2':
            if not selected_person.phone_numbers:
                print("No phone numbers to update.")
                continue

            for idx, phone in enumerate(selected_person.phone_numbers, 1):
                print(f"{idx}. {phone}")

            index_to_update = input("Select a phone number to update (or press Enter to cancel): ")
            if index_to_update.isdigit():
                index_to_update = int(index_to_update)
                if 1 <= index_to_update <= len(selected_person.phone_numbers):
                    new_phone_number = input("Enter the new phone number: ")
                    if len(new_phone_number) in [7, 10] and new_phone_number.isdigit():
                        selected_person.phone_numbers[index_to_update - 1] = new_phone_number
                        print(f"Phone number updated to {new_phone_number}.")
                    else:
                        print("Invalid phone number format.")
            else:
                print("Canceled update.")

        elif choice == '3':
            break

        else:
            print("Invalid option selected.")
