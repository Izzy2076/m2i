class Person: 
    def __init__(self, name, email): 
        self.name = name 
        self.email= email 
        
    def show(self): 
        print(self.name + ' - ' + self.email)