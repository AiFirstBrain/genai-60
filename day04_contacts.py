import json
try:    
    with open("contacts.json","r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts ={}        
while True:
    cmd = input("choose add/list/quit/find/delete: ")
    if cmd == "quit":
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
            
        break
    elif cmd == "add":
        name = input("name: ")
        phone = input("contact: ")
        contacts[name] = phone
        print("added contact")

    elif cmd == "list":
        for name in contacts:
            print(f"{name}: {contacts[name]}")  
    elif cmd == "find":
        name = input("name: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
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
        