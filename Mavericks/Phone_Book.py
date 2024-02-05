def menu():
    print("Welcome!!!")
    print("Choose a number to perform any service")
    print("1. Add new contact")
    print("2. Display all contacts")
    print("3. Delete contact")
    print("4. Exit")


contactName = []
contactPhoneNumber = []


def add_new_contact(name, phoneNumber):
    contactName.append(name)
    contactPhoneNumber.append(phoneNumber)


def display_all_contact():
    if not contactName:
        print("No contact found ")
    else:
        for contact in range(len(contactName)):
            print(contactName[contact], contactPhoneNumber[contact])


def delete_contact(name, phoneNumber):
    for contact in contactName:
        if contact == name:
            contactName.remove(contact)

    for contact in contactPhoneNumber:
        if contact == phoneNumber:
            contactPhoneNumber.remove(contact)


def exit():
    print("__________________________________________________________________")
    print("Thank you for using my phoneBook!!!")
    print("___________________________________________________________________")
    print("Have a nice day!!!")


menu()
option = int(input("Please enter your choice:"))
if (option == 1):
    name = str(input("Enter name:"))
    phoneNumber = str(input("Enter phone number:"))
    add_new_contact(name, phoneNumber)

    display_all_contact()
if (option == 2):
    display_all_contact()

if (option == 3):
    name = str(input("Enter name:"))
    phoneNumber = str(input("Enter phone number:"))
    delete_contact(name, phoneNumber)
    print("Phone_Number deleted")

if (option == 4):
    print("__________________________________________________________________")
    print("Thank you for using my phoneBook!!!")
    print("___________________________________________________________________")
    print("Have a nice day!!!")




