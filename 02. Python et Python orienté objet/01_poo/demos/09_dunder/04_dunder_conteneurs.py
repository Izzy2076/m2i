class Address: 
  def __init__(self, street, city): 
      self.street = str(street) 
      self.city = str(city) 
      
  def show(self): 
      print(self.street) 
      print(self.city)

class Person: 
    def __init__(self, name, email): 
        self.name = name 
        self.email= email 
        
    def show(self): 
        print(self.name + ' - ' + self.email)

class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    def show(self):
        Person.show(self)
        Address.show(self)

class Notebook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, email, street, city):
        self.contacts[name] = Contact(street, city, name, email)

    def show(self):
        for name, contact in self.contacts.items():
            print(f"=== {name} ===")
            contact.show()

    def __contains__(self, name): # "Alice" in notebook
        if name in self.contacts:
            print(f"{name} est dans le notebook")
        else:
            print(f"{name} n'est pas dans le notebook")

    def __len__(self):
        return len(self.contacts)
    
    def __delitem__(self, name):
        print(f"{name} supprimé des contacts")
        del self.contacts[name]


notes = Notebook() 
notes.add('Alice', '<alice@example.com>', 'Lv 24', 'Sthlm') 
notes.show()
print(len(notes))

del notes["Alice"]
"Alice" in notes
