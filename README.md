Person Management System
======================================

This project is a simple command-line person management system written in Python. It allows users to create, view, update, and delete person records, including additional information like phone numbers and email addresses. The program offers an interactive menu to navigate through various options to manage the data.

Features
--------

### Main Menu Options:

1.  **Add Person**
2.  **List People**

* * * * *

### 1\. Add Person

Allows the user to add a new person to the system.

**Steps:**

-   Enter the name (required).
-   Optionally add Date of Birth (DOB).
-   Optionally add phone numbers.
    -   Enter phone numbers one by one.
    -   Option to add multiple phone numbers.
-   Optionally add email addresses.
    -   Enter email addresses one by one.
    -   Option to add multiple email addresses.
-   After adding the person, a report is generated displaying the created person's details.

* * * * *

### 2\. List People

Displays a list of people stored in the system.

**Steps:**

-   View a list of people with their assigned IDs.

    -   Example:
        1.  Brandon
        2.  Nodnarb
-   Select a person by ID to view their details.

    -   **Person Details**:
        -   Name
        -   Date of Birth (DOB)
        -   Phone Numbers
        -   Email Addresses
-   After viewing a person, you are presented with additional options:

    **View Person Options**:

    1.  **Update**
        -   Update Name
        -   Update Date of Birth (DOB)
        -   Update Phone Numbers
            -   Add phone numbers
            -   Edit existing phone numbers
        -   Update Email Addresses
    2.  **Delete**: Remove the person from the system.

* * * * *

### Update Person Details

Once a person is selected, the following updates are available:

-   **Edit Name**
    -   Enter a new name (required).
-   **Edit Date of Birth**
    -   Enter a new Date of Birth (optional).
-   **Update Phone Numbers**
    -   **Add Phone Number**: Allows you to add additional phone numbers.
    -   **Edit Phone Numbers**: View and edit existing phone numbers. Phone numbers should be integers of length between 7 and 10 digits.
-   **Update Email Addresses**
    -   **Add Email**: Allows you to add additional email addresses.
    -   **Edit Emails**: View and edit existing email addresses.

* * * * *

Requirements
------------

-   Python 3.x
-   SQLite database (included in the project)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/person-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd person-management-system
    ```

3. Install any required dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```


Usage
-----

Follow the on-screen prompts to navigate through the menus and manage the people in the system.

Future Enhancements
-------------------

-   Improve validation for inputs such as phone numbers and email addresses.
-   Add search functionality to find people by name or other attributes.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Author
------

-   **Brandon Collins**
    -   GitHub: [b-randon-collins](https://github.com/b-randon-collins)