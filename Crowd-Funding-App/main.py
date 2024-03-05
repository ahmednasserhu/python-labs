from registration import register
from login import validate_login
from campaign import create_campaign, view_campaigns, edit_campaign, delete_campaign
import os

current_user = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    print("Welcome to Crowdfunding App!")
    print("----------------------------")

def print_menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def print_project_menu():
    print("1. Create a Project")
    print("2. View All Projects")
    print("3. Edit My Projects")
    print("4. Delete My Project")
    print("5. Logout")

def registartion():
    clear_screen()
    print_welcome()
    print("Registration\n")
    register()

def login():
    global current_user
    clear_screen()
    print_welcome()
    print("Login\n")
    current_user = validate_login()

def create_project():
    clear_screen()
    print_welcome()
    print("Create a Project\n")
    create_campaign(current_user)

def view_all_projects():
    clear_screen()
    print_welcome()
    print("View All Projects\n")
    view_campaigns(current_user)

def edit_my_projects():
    clear_screen()
    print_welcome()
    print("Edit My Projects\n")
    edit_campaign(current_user)

def delete_my_project():
    clear_screen()
    print_welcome()
    print("Delete My Project\n")
    delete_campaign(current_user)

while True:
    clear_screen()
    print_welcome()
    print_menu()

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        registartion()
    elif choice == "2":
        login()
        if current_user:
            while True:
                clear_screen()
                print_welcome()
                print_project_menu()

                project_choice = input("Enter your choice (1-5): ")

                if project_choice == "1":
                    create_project()
                elif project_choice == "2":
                    view_all_projects()
                elif project_choice == "3":
                    edit_my_projects()
                elif project_choice == "4":
                    delete_my_project()
                elif project_choice == "5":
                    current_user = None
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
    elif choice == "3":
        print("Exiting the Crowdfunding App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")