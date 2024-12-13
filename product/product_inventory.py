from pprint import pprint

class Inventory:
    def __init__(self):
        self.product_inventory = {}

    def add_product(self, product):
        self.product_inventory[product.id] = product.__dict__

    def delete_product_by_name(self,product_id):
        del_product = self.product_inventory.pop(product_id, None)
        if del_product :
            print(f"Product with ID: {product_id} removed")
        else:
            print(f"Product with ID: {product_id} not found")

    def update_product_quantity(self, product_id, quantity):
        if product_id in self.product_inventory:
            new_quantity = self.product_inventory[product_id]['quantity'] - quantity
            self.product_inventory[product_id]['quantity']=new_quantity
            print(f"New quantity for product {product_id} is {new_quantity}")
        else:
            print(f"Product {product_id} not found")
    
    def show_inventory(self):
        pprint(self.product_inventory)

    def get_price_by_id(self, product_id):
        if product_id in self.product_inventory:
            return self.product_inventory[product_id]["price"]
        else:
            print(f"Producto {product_id} no encontrado")

    def get_stock_by_id(self, product_id):
        if product_id in self.product_inventory:
            return self.product_inventory[product_id]["quantity"]
        else:
            print(f"Producto {product_id} no encontrado")

    def get_have_stock(self, product_id, quantity):
        if product_id in self.product_inventory:
            return  quantity <= int(self.product_inventory[product_id]["quantity"])
        else:
            print(f"Producto {product_id} no encontrado")