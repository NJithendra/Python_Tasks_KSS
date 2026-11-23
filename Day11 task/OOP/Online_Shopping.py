#Online Shopping System (Multilevel Inheritance)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class ElectronicProduct(Product):
    def display_electronic(self):
        print("Product:", self.name)
        print("Price:", self.price)
class MobilePhone(ElectronicProduct):
    def display(self):
        self.display_electronic()
        print("Category: Mobile Phone")
m = MobilePhone("Samsung", 25000)
m.display()
