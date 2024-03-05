def validate_login():
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        email = input('Enter your email: ')
        password = input('Enter your password: ')

        if not email.strip() or not password.strip():
            print("You didn't enter the email or the password or both of them. Please try again.")
        else:
            with open('user_data.txt', 'r') as file:
                for line in file:
                    stored_email, stored_password = map(str.strip, line.strip().split(':')[2:4])
                    if stored_email == email and stored_password == password:
                        print("Login successful!")
                        return email

                attempts += 1
                print(f"Email or password is incorrect. Attempt {attempts}/{max_attempts}. Please try again.")

    print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")
    return None
