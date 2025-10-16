import string
import random
import os

def new_pass():
    print("\n--- Welcome 'new-password' section ---")
    passWord = input("Do you need to create a new-pass (yes/no): ").lower()
    
    if passWord == 'no':
        return None
    elif passWord == 'yes':
        print("\nYou can create your own new-pass: ")
        try:
            Password = int(input("Enter your password length (minimum 8 characters): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

        if Password >= 8:
            char = string.ascii_letters + string.punctuation + string.digits
            PassWord = "".join(random.choice(char) for _ in range(Password))
            print("Your password: " + PassWord)
            return PassWord
        else:
            print("Your length is short! Minimum is 8 characters.")
            return None
    else:
        print("Thank you!")
        return None

def save_acc():
    print("\n--- Welcome 'save_acc' section ---")
    confirm = input("Are you a new person (yes/no): ").lower()

    if confirm == "no":
        print("\nGo to login section and login.....!")
    elif confirm == "yes":
        username = input("Enter username: ")
        password = new_pass()
        if password:
            with open("pass.txt", "a", encoding="utf-8") as f:
                f.write(f"Username: {username}, Password: {password}\n")
            print("Account saved successfully!")
        else:
            print("Account not saved due to password issue.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

def view_acc():
    print("\n--- Welcome 'view_acc' section ---")
    if not os.path.exists("pass.txt"):
        print("No accounts saved yet!")
        return

    with open("pass.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        if not lines:
            print("File is empty!")
            return
        for i, acc in enumerate(lines, start=1):
            print(f"{i}. {acc.strip()}")

# Main loop
while True:
    print("\n--- Password Manager ---")
    print("1. Generate new password")
    print("2. Save account")
    print("3. View accounts")
    print("4. Exit")

    action = input("Enter your action (1-4): ")

    if action == '1':
        new_pass()
    elif action == '2':
        save_acc()
    elif action == '3':
        view_acc()
    elif action == '4':
        print("Thank you for using me.... Goodbye!")
        break
    else:
        print("Invalid action... Please try again!")