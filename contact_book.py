import os
import json
from datetime import datetime

contacts = []
class Contact:
    def __init__(self):
        pass

    def add_contact(self):
        print("\n---Welcome to Add Contacts section ---")
        name = input("Enter your name: ")
        phone_number = input("Enter your mobile number: ")
        email = input("Enter your email: ")

        entry = {
            "Name" : name,
            "Phone Number" : phone_number,
            "Email" : email
        }

        contacts.append(entry)

        if os.path.exists("contacts.json"):
            print("contacts.json file exists.")
        else:
            print("contacts.json file not found.")
        
        print("Your details successfully saved.!")

    def search_contact(self):
        print("\n--- Welcome to Search Contact section ---")
        if not contacts:
            print("No contacts saved in contacts app.!")

        for i, n in enumerate(contacts, start=1):
            print(f"{i}. {n}")

        try:
            name1 = input("Enter your name: ")
            if name1 in contacts:
                print(contacts)
            else:
                print(name1 + "is not in contacts")
        except ValueError:
            print("Invalid error format!")
    
    def delete_contact(self):
        print("\n--- Welcome to Delete Contact section ---")
        if not contacts:
            print("No contacts saved in contacts app.!")

        for i, n in enumerate(contacts, start=1):
            print(f"{i}. {n}")

        dlt = input("Do you need to delete (all/one) contacts: ").lower()
        try:
            if dlt == "all":
                contacts.clear()
                print("Your all contacts deleted successfully!")
            elif dlt == "one":
                delete = input(f"Select for which you need to delete {i}: ")
                