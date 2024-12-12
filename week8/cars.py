class Cars:
    def display_details(self):
        print("Car details: Company:", self.company, ", Price:", self.price, ", Color:", self.color)
car1 = Cars()
car1.company = "Toyota"
car1.price = 25000
car1.color = "Red"

car2 = Cars()
car2.company = "Honda"
car2.price = 22000
car2.color = "Blue"

car3 = Cars()
car3.company = "Ford"
car3.price = 28000
car3.color = "Black"

car1.display_details()
car2.display_details()
car3.display_details()

            
