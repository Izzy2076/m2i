from classes.OrderSystem import OrderSystem

products_path = "./exercices/tp_vendredi/datas/products.csv"
orders_path = "./exercices/tp_vendredi/datas/orders.csv"
orderSystem = OrderSystem()

orderSystem.load_products(products_path)
orderSystem.load_orders(orders_path)
orderSystem.display_orders()
orderSystem.display_products()

order = orderSystem.add_order(1, 4, "Toto")
if order:
    print(f"Commande ajoutée {order}")
else:
    print("Stock insuffisant ou produit introuvable")

orderSystem.save_orders(orders_path)
orderSystem.save_products(products_path)