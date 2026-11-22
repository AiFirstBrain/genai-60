from storage import load_contacts, save_contacts, Contact
contacts = load_contacts()      
while True:
    cmd = input("choose add/list/quit/find/delete: ")
    if cmd == "quit":
        save_contacts(contacts)
        break
    elif cmd == "add":
        name = input("name: ")
        phone = input("contact: ")
        cleaned = phone.replace(" ","").replace("+", "")
        try:
            int(cleaned)
            print("added contact")
            contacts[name] = phone
        except ValueError:
            print("Phone must be digits only.")    
        
        

    elif cmd == "list":
        for name in contacts:
            c = Contact(name,contacts[name])
            print(c.display())    
    elif cmd == "find":
        name = input("name: ")
        if name in contacts:
            c = Contact(name,contacts[name])
            print(c.display())
        else:
            print("Not found")
    elif cmd == "delete":
        name = input("name: ")
        if name in contacts:
            del contacts[name]
            print("Deleted")  
        else:
            print("Not found")              
    else:
        print("Unknown command")          
        