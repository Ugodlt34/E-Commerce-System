class Product:
    def __init__(self, product_name, product_id, price, stock_quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            return True
        return False

    def get_product_details(self):
        return f"{self.product_name} - {self.price}€, Stock: {self.stock_quantity}"