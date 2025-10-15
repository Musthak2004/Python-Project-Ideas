import string
import random

def new_pass():
    print("\n--- Welcome 'new-password' section ---")
    passWord = input("Do you need to create a new-pass (yes/no): ").lower()
    
    if passWord == 'no':
        return
    elif passWord == 'yes':
        print("\nYou can create your own new-pass: ")
        try:
            Password = int(input("Enter your password length (minimum 8 characters): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if Password >= 8:
            char = string.ascii_letters + string.punctuation + string.digits
            PassWord = "".join(random.choice(char) for _ in range(Password))
            print("Your password: " + PassWord)
        else:
            print("Your length is short! Minimum is 8 characters.")
    else:
        print("Thank you!")

    
def save_acc():
    print("\n--- Welcome 'save_acc' section ---")
    confirm = input("Are you a new person (yes/no): ").lower()

    if confirm == "no":
        