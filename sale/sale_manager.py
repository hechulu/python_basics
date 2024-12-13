class SaleManager:
    def __init__(self):
        self.sales = []

    def register_sale(self, new_sale):
        self.sales.append(new_sale.__dict__)

    def show_sales(self):
        print(self.sales)
        