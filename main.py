import asyncio

from product.product_inventory import Inventory
from product.product_model import Product
from sale.sale_model import Sale
from sale.sale_manager import SaleManager
from payment.payment_manager import Payment

async def main():
    product_inventory = Inventory()
    sale_manager = SaleManager()
    new_sale = Sale()
    new_sale2 = Sale()
    payment = Payment()

    product_inventory.add_product(Product(1,"Papas",20.00,5))
    product_inventory.add_product(Product(2,"Refresco",7.00,10))
    product_inventory.add_product(Product(3,"Gelatina",15.50,8))
    product_inventory.add_product(Product(4,"Jabon",25.80,25))
    product_inventory.show_inventory()

    new_sale.add_product(1,2,product_inventory)
    new_sale.add_product(2,3,product_inventory)
    new_sale.add_product(3,8,product_inventory)
    new_sale.add_product(3,1,product_inventory)

    new_sale.show_sale()

    new_sale2.add_product(1,3,product_inventory)
    new_sale2.add_product(2,5,product_inventory)
    new_sale2.add_product(4,15,product_inventory)

    new_sale2.show_sale()

    sale_manager.register_sale(new_sale)
    sale_manager.register_sale(new_sale2)

    sale_manager.show_sales()

    product_inventory.show_inventory()

    await payment.process_payment(new_sale.get_total())

    await payment.process_payment(new_sale2.get_total())

if __name__ == "__main__":
     asyncio.run(main())