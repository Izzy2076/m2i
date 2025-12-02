from classes.Address import Address
from classes.Person import Person

class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    def show(self):
        Person.show(self)
        Address.show(self)