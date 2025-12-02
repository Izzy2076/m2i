class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - disponible : {self.stock} - prix : {self.price}"
    
    def change_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False