def menu():
    print("Welcome!!!")
    print("Choose a number to perform any service")
    print("1. Add new contact")
    print("2. Display all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")


contactName = []
contactPhoneNumber = []


def add_new_contact(name, phoneNumber):
    contactName.append(name)
    contactPhoneNumber.append(phoneNumber)
    if len(phoneNumber) != 11:
        print("Invalid number!!! Kindly enter 11 digit number")


def display_all_contact():
    if not contactName:
        print("No contact found ")
    else:
        for contact in range(len(contactName)):
            print(contactName[contact], contactPhoneNumber[contact])

def search_contact(name):
    for contact in contactName:
        if name == contact:
            return contact
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





