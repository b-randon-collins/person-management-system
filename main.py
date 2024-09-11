# main.py
from db import initialize_database, engine
from navigation_options.main_menu import main_menu

initialize_database()

main_menu()
