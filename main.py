from Mavericks.Phone_Book import *

menu()
option = int(input("Please enter your choice:"))
if option == 1:
    name = str(input("Enter name:"))
    phoneNumber = str(input("Enter phone number:"))
    add_new_contact(name, phoneNumber)

    display_all_contact()
if option == 2:
    display_all_contact()

if option == 3:
    name = str(input("Enter name:"))
    search_contact(name)


if option == 4:
    name = str(input("Enter name:"))
    phoneNumber = str(input("Enter phone number:"))
    delete_contact(name, phoneNumber)
    print("Phone_Number deleted")

if option == 5:
    print("__________________________________________________________________")
    print("Thank you for using my phoneBook!!!")
    print("___________________________________________________________________")
    print("Have a nice day!!!")



