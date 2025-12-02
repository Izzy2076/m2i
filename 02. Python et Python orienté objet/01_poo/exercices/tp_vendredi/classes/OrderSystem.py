from classes.Order import Order
from classes.Product import Product
import csv

class OrderSystem:
    def __init__(self):
        self.products : Product = []
        self.orders : Order = []
        self.new_id = 1

    def load_products(self, path):
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)
            for value in reader:
                id, name, price, quantity = value
                product = Product(int(id), name, float(price), int(quantity))
                self.products.append(product)

    def load_orders(self, path):
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)
            for value in reader:
                order_id, product_id, quantity, customer = value
                order = Order(int(order_id), int(product_id), int(quantity), customer)
                self.orders.append(order)
    
    def display_products(self):
        for product in self.products:
            print(product)
    
    def display_orders(self):
        for order in self.orders:
            print(order)

    def save_products(self, path):
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["id","name","price","stock"])
            for product in self.products:
                writer.writerow([product.id, product.name, product.price, product.stock])
    
    
    def save_orders(self, path):
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["order_id","product_id","quantity","customer"])
            for order in self.orders:
                writer.writerow([order.order_id, order.product_id, order.quantity, order.customer])

    def get_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def add_order(self, product_id, quantity, customer):
        product = self.get_product(product_id)
        if product and product.change_stock(quantity):
            order = Order(self.new_id, product_id, quantity, customer)
            self.orders.append(order)
            self.new_id += 1
            return order
        return None