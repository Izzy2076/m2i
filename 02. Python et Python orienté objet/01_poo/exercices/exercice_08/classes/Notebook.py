from classes.Contact import Contact

class Notebook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, email, street, city):
        self.contacts[name] = Contact(street, city, name, email)

    def show(self):
        for name, contact in self.contacts.items():
            print(f"=== {name} ===")
            contact.show()