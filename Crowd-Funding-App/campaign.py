from datetime import datetime
import os

def create_campaign(username):
    print(f"Welcome, {username}! You are now logged in.")
    
    title = input('Enter the campaign title: ')
    details = input('Enter the campaign details: ')
    target_amount = input('Enter the total target amount: ')
    
    while True:
        try:
            start_date = input('Enter the start date (YYYY-MM-DD): ')
            end_date = input('Enter the end date (YYYY-MM-DD): ')
            start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
            end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start_datetime >= end_datetime:
                raise ValueError("End date must be later than start date.")
            
            break
        except ValueError as e:
            print(f"Invalid date format or {e}. Please try again.")

    user_folder = os.path.join(os.getcwd(), username)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    filename = os.path.join(user_folder, f"{title}_campaign.txt")
    with open(filename, 'w') as file:
        file.write(f"{title}:{details}:{target_amount}:{start_date}:{end_date}\n")

    print(f"Campaign created successfully.")

def view_campaigns(username):
    user_folder = os.path.join(os.getcwd(), username)

    try:
        files = os.listdir(user_folder)

        if files:
            print(f"Campaigns for {username}:")
            for i, filename in enumerate(files, 1):
                with open(os.path.join(user_folder, filename), 'r') as file:
                    campaign_details = file.readline().strip()
                    print(f"{i}. {campaign_details}")

            input("Press Enter to exit the view. ")
        else:
            print(f"No campaigns found for {username}.")
    except FileNotFoundError:
        print(f"No campaigns found for {username}.")

def get_campaign(username):
    view_campaigns(username)
    
    try:
        campaign_number = int(input("Enter the number of the campaign to edit or delete (enter 0 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

    user_folder = os.path.join(os.getcwd(), username)
    try:
        files = os.listdir(user_folder)

        if 1 <= campaign_number <= len(files):
            filename = os.path.join(user_folder, files[campaign_number - 1])
            return filename
        elif campaign_number == 0:
            print("Exiting the edit menu.")
            return None
        else:
            print("Invalid campaign number. Please enter a valid number.")
            return None
    except FileNotFoundError:
        print(f"No campaigns found for {username}.")
        return None
      
def get_new_campaign_details(existing_campaign):
    with open(existing_campaign, 'r') as file:
        edited_campaign = file.readline().strip().split(':')
        print(f"Editing campaign: {edited_campaign}")

    while True:
        print("\nChoose what to edit:")
        print("1. Title")
        print("2. Details")
        print("3. Target Amount")
        print("4. Start Date")
        print("5. End Date")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            edited_campaign[0] = input(f"Enter the new title ({edited_campaign[0]}): ")
        elif choice == "2":
            edited_campaign[1] = input(f"Enter the new details ({edited_campaign[1]}): ")
        elif choice == "3":
            edited_campaign[2] = input(f"Enter the new target amount ({edited_campaign[2]}): ")
        elif choice == "4":
            edited_campaign[3] = get_valid_date_input(f"Enter the new start date (YYYY-MM-DD) ({edited_campaign[3]}): ")
        elif choice == "5":
            edited_campaign[4] = get_valid_date_input(f"Enter the new end date (YYYY-MM-DD) ({edited_campaign[4]}): ")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    return edited_campaign

def get_valid_date_input(prompt):
    while True:
        try:
            date_input = input(prompt)
            datetime.strptime(date_input, '%Y-%m-%d')
            return date_input
        except ValueError as e:
            print(f"Invalid date format or {e}. Please try again.")

def save_edited_campaign(existing_campaign, edited_campaign):
    with open(existing_campaign, 'w') as file:
        file.write(f"{':'.join(edited_campaign)}\n")

    print("Campaign edited successfully.")

def edit_campaign(username):
    existing_campaign = get_campaign(username)

    if existing_campaign:
        edited_campaign = get_new_campaign_details(existing_campaign)
        save_edited_campaign(existing_campaign, edited_campaign)

def delete_campaign(username):
    campaign_to_delete = get_campaign(username)

    if campaign_to_delete:
        confirm_delete = input(f"Are you sure you want to delete the campaign? (yes/no): ").lower()

        if confirm_delete == "yes":
            os.remove(campaign_to_delete)
            print("Campaign deleted successfully.")
        else:
            print("Campaign deletion canceled.")
