class Order:
    def __init__(self, order_id, product_id, quantity, customer):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer = customer

    def __str__(self):
        return f"Commande n°{self.order_id} - {self.customer} : {self.product_id} - {self.quantity}"