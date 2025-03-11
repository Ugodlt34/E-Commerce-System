class Cart:
    def __init__(self, user):
        self.user = user
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.items[product.product_id] = (product, quantity)
            return "Product added to cart."
        return "Not enough stock."

    def remove_product(self, product):
        if product.product_id in self.items:
            del self.items[product.product_id]
            return "Product removed from cart."
        return "Product not in cart."

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.values())
