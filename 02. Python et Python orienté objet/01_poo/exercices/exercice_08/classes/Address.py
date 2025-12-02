class Address: 
  def __init__(self, street, city): 
      self.street = str(street) 
      self.city = str(city) 
      
  def show(self): 
      print(self.street) 
      print(self.city)