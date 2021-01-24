class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Suthinan"
customer1.lastName = "Phantharak"
customer1.addCart()

customer2 = Customer()
customer2.name = "Alin"
customer2.lastName = "Waengphula"
customer2.addCart()