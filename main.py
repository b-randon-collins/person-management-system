from db import initialize_database, engine
from main_menu import main_menu

initialize_database()

main_menu()

engine.dispose()
