class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity
        return self.stock[item]

    def remove_stock(self, item, quantity):
        if item not in self.stock or self.stock[item] < quantity:
            raise ValueError("Insufficient stock")
        self.stock[item] -= quantity
        return self.stock[item]

    def check_availability(self, item, quantity):
        return self.stock.get(item, 0) >= quantity
i=Inventory()
print(i.add_stock("AAPL", 10))
print(i.remove_stock("AAPL", 5))
print(i.check_availability("AAPL", 5))