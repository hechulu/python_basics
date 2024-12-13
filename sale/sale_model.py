from pprint import pprint
from product.product_inventory import Inventory
from datetime import datetime

class Sale:
    def __init__(self):
        self.date = datetime.now()
        self.products = []
        self.total =0

    def add_product(self,product_id, quantity, inventory : Inventory):
        if inventory.get_have_stock(product_id,quantity):
            inventory.update_product_quantity(product_id,quantity)
            price = inventory.get_price_by_id(product_id)
            self.products.append({product_id : {"quantity" : quantity, "sale_price" : price}})
            self.total = self.total + (price * quantity)
        else:
            print(f"Product {product_id} not have {quantity} pices")

    def get_total(self):
        return self.total

    def show_sale(self):
        pprint(self.__dict__)