import json
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)
def load_contacts():
    try:    
        with open("contacts.json","r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        print("no saved contacts yet. Starting a new book")
        contacts ={}   
    except json.JSONDecodeError:
        print("json file is corrupt.starting empty")  
        contacts = {} 
    return contacts
class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone 
    def display(self):
        return f"{self.name}: {self.phone}"     
