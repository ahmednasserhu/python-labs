
import re

def validate_fname():
    while True:
        fname = input("Enter your first name: ")

        if not fname.isalpha():
            print("Invalid input. Your first name should contain only alphabetical characters. Please try again.")
        else:
            return fname.strip()
        
def validate_lname():
    while True:
        lname = input("Enter your last name: ")
        if not lname.isalpha():
            print("Invalid input. Your last name should contain only alphabetical characters. Please try again.")
        else:
            return lname.strip()

def validate_email():
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    while True:
        email = input('Enter your email: ')
        if not email.strip():
            print("You didn't enter any input. Please try again.")
        elif not email_pattern.match(email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            with open('user_data.txt', 'r') as file:
                for line in file:
                    stored_email = line.strip().split(':')[2]
                    if stored_email == email:
                        print('This email exists. Please enter another one.')
                        break
                else:
                    return email

def validate_password():
    while True:
        password = input('Enter your password: ')

        if not password.strip():
            print("You didn't enter any input. Please try again.")
        elif len(password) < 8:
            print("Password should be at least 8 characters long. Please try again.")
        elif not any(char.isdigit() for char in password):
            print("Password should contain at least one digit. Please try again.")
        else:
            confirm_password = input('Please confirm your password: ')

            if confirm_password != password:
                print("Passwords do not match. Please try again.")
            else:
                return password

def validate_mobile():
    while True:
        phone = input('Enter your phone number: ')
        if not phone.strip():
            print("You didn't enter any input. Please try again.")
        elif not phone.isdigit():
            print('Please enter only numbers.')
        elif len(phone) > 11:
            print("Invalid phone number.")
        elif phone[:3] not in ['011','012','010','015']:
            print('This phone number is not valid in egypt please enter a valid one.')
        else:
            return phone
        
def register():
    fname = validate_fname()
    lname = validate_lname()
    email = validate_email()
    password = validate_password()
    phone = validate_mobile()

    with open('user_data.txt', 'a') as file:
        file.write(f"{fname}:{lname}:{email}:{password}:{phone}\n")
        
    print("User registerd successfully, please login now.")
