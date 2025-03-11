class Order:
    def __init__(self, order_id, user, items):
        self.order_id = order_id
        self.user = user
        self.items = items
        self.status = "Processing"

    def place_order(self):
        self.user.order_history.append(self)
        return "Order placed successfully."

    def update_status(self, new_status):
        self.status = new_status
        return f"Order status updated to {new_status}."
