contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

add_contact("Alice", "123-456-7890")
view_contacts()
