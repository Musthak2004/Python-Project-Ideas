import os
import json

contacts = []

# Load existing contacts
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as file:
        contacts = json.load(file)

class Contact:
    def add_contact(self):
        print("\n--- Add Contact ---")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        entry = {"Name": name, "Phone": phone, "Email": email}
        contacts.append(entry)

        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contact saved successfully!")

    def search_contact(self):
        print("\n--- Search Contact ---")
        name1 = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["Name"].lower() == name1.lower():
                print("Found:", contact)
                found = True
                break
        if not found:
            print(name1 + " is not in contacts")

    def delete_contact(self):
        print("\n--- Delete Contact ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact}")

        try:
            choice = input("Delete (all/one): ").lower()
            if choice == "all":
                contacts.clear()
                print("All contacts deleted.")
            elif choice == "one":
                index = int(input("Enter contact number to delete: ")) - 1
                if 0 <= index < len(contacts):
                    contacts.pop(index)
                    print("Contact deleted.")
                else:
                    print("Invalid index.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid value input.")

        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)

    def exit_app(self):
        print("Thank you for using Contacts App!")

# Main loop
c = Contact()
while True:
    print("\n--- Contacts Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    option = input("Enter your choice: ")
    if option == "1":
        c.add_contact()
    elif option == "2":
        c.search_contact()
    elif option == "3":
        c.delete_contact()
    elif option == "4":
        c.exit_app()
        break
    else:
        print("Invalid choice!")