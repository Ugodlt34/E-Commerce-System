class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Encapsulation
        self.order_history = []

    def register(self):
        return f"User {self.username} registered successfully."

    def login(self, password):
        return self.__password == password

    def view_order_history(self):
        return self.order_history