# Name: Lam Doan
# # Date: 10/17/2024
# File Purpose: main

from contacts import *

my_contact = Contacts(filename = "contacts.json")


while True:
    print("           *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("     1. Add contact")
    print("     2. Modify contact")
    print("     3. Delete contact")
    print("     4. Print contact list")
    print("     5. Set contact filename")
    print("     6. Exit the program")
    
    menu = int(input("\n     Enter menu choice: "))
    if menu < 1 or menu >= 6:
        break
    elif menu == 1:
        phone_number = str(input("\n     Enter phone number: "))
        first        = str(input("     Enter first name: "))
        last         = str(input("     Enter last name: "))
        res = my_contact.add_contact(id = phone_number, last_name = last, first_name = first)
        if res == "error":
            print("     Phone number already exists.\n")
        else:
            print(f"     Added: {first} {last}.\n")
    elif menu == 2:
        phone_number = str(input("\n     Enter phone number: "))
        first        = str(input("     Enter first name: "))
        last         = str(input("     Enter last name: "))
        res = my_contact.modify_contact(id = phone_number, last_name = last, first_name = first)
        if res == "error":
            print("     Invalid phone number.\n")
        else:
            print(f"     Modified: {first} {last}.\n")
    elif menu == 3:
        phone_number = str(input("\n     Enter phone number: "))
        res = my_contact.delete_contact(id = phone_number)
        if res == "error":
            print("     Invalid phone number.\n")
        else:
            print(f"     Deleted: {res[0]} {res[1]}.\n")
    elif menu == 4:
        my_contact.print_contact()
    elif menu == 5:
        new_filename = str(input("\n     Enter new filename: "))
        my_contact.__init__(filename=new_filename)
        print(f"     Filename set to: {new_filename}\n")