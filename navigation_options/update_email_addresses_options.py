def update_email_addresses_options(selected_person):
    while True:
        print("\nUpdate Email Addresses")
        print("1. Add Email Address")
        print("2. Update Existing Email Addresses")
        print("3. Return to Update Person Options")

        choice = input("\nSelect an option: ")

        if choice == '1':
            while True:
                email_address = input("Enter Email Address: ")
                if "@" in email_address and "." in email_address:
                    selected_person.email_addresses.append(email_address)
                    print(f"Email address {email_address} added.")
                    add_more = input("Add another? (y/n): ")
                    if add_more.lower() != 'y':
                        break
                else:
                    print("Invalid email format. Please try again.")

        elif choice == '2':
            if not selected_person.email_addresses:
                print("No email addresses to update.")
                continue

            for idx, email in enumerate(selected_person.email_addresses, 1):
                print(f"{idx}. {email}")

            index_to_update = input("Select an email address to update (or press Enter to cancel): ")
            if index_to_update.isdigit():
                index_to_update = int(index_to_update)
                if 1 <= index_to_update <= len(selected_person.email_addresses):
                    new_email = input("Enter the new email address: ")
                    if "@" in new_email and "." in new_email:
                        selected_person.email_addresses[index_to_update - 1] = new_email
                        print(f"Email address updated to {new_email}.")
                    else:
                        print("Invalid email format.")
            else:
                print("Canceled update.")

        elif choice == '3':
            break

        else:
            print("Invalid option selected.")
