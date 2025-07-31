contacts=[
    {"NAME":"AHMAD","CONTACT":"0301 1234567"},
    {"NAME":"ABDULLAH","CONTACT":"0302 1234567"},
    {"NAME":"BILAL","CONTACT":"0303 1234567"},
    {"NAME":"IMAN","CONTACT":"0304 1234567"},
    {"NAME":"MARIA","CONTACT":"0305 1234567"},
    {"NAME":"HADIA","CONTACT":"0306 1234567"},
    {"NAME":"ABDULL AHAD","CONTACT":"0307 1234567"},
    {"NAME":"LAIBA","CONTACT":"0308 1234567"},
    {"NAME":"SHEHZAD","CONTACT":"0309 1234567"}
]
def addcon():
    n=str(input("WRITE NAME FOR NEW CONTACT:- "))
    c=str(input("WRITE THE NUMMBER OF NEW CONTACT:- "))
    contacts.append({"NAME":n,"CONTACT":c})
    print(f"CONGRATULATIONS NEW CONTACT {n} IS ADDED")

def viewcon():
    print("\n{:<3} {:<15} {:<15}".format("No", "Name", "Contact Number"))
    print("-" * 40)
    for index, contact in enumerate(contacts, start=1):
        name = contact.get("NAME")
        phone = contact.get("PHONE") or contact.get("CONTACT", "N/A")
        print("{:<3} {:<15} {:<15}".format(index, name, phone))

def searchcon():
    item=input("WRITE THE CONTACT:- ").lower()
    found=False
    for contact in contacts:
        if contact.get("NAME","").lower()==item:
            number=contact.get("CONTACT") or contact.get("PHONE","NOT FOUND")
            print(f"YES {item} IS IN YOUR CONTACT. NUMBER:{number}")
            found=True
            break
    if not found:
        print(f"NO {item} IS NOT IN YOUR CONTACT")

def delcon():
    name_to_dlt=input("WRITE THE NAME FOR DELETE:- ").lower()
    found=False
    for contact in contacts:
        if contact["NAME"].lower()==name_to_dlt:    
            contacts.remove(contact)
            print(f"YOUR CONTACT {name_to_dlt} IS DELETED SUCESSFULLY WITH {contact.get("PHONE")}")
            found=True
            break
    if not found:
        print("WRITE CORRECT NAME OF CONTACT")
    
def savefile():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            print("Saving contact:", contact)
            file.write(f"Name: {contact.get('NAME','N/A')}, Phone: {contact.get('CONTACT','N/P')}\n")
    print("Contacts saved to contact.txt")


while True:
        print("-"*40 + "WELCOME TO THE CONTACT BOOK"+"-"*40)
        print("1.ADD NEW CONTACT")
        print("2.VIEW ALL CONTACT")
        print("3.SEARCH CONTACT BY NAME")
        print("4.DELETE CONTACT")
        print("5.WANT CONTACT FILE AS IN TEXT")
        C=int(input("WRITE THE SERVICE YOU WANT(1-5):- "))
        match C:
            case 1:
                addcon()
            case 2:
                viewcon()
            case 3:
                searchcon()
            case 4:
                delcon()
            case 5:
                savefile()
            case _:
                print("INVALID CHOICE")

