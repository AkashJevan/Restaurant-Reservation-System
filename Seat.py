#Defining seat n properties
class Seat:
    #Setting void seat
    def __init__(self):
        self.customer = None
        self.price = 0

    #Reserve customer n price for seat
    def reserve(self, customer, price):
        self.customer = customer
        self.price = price
        
    #Emty seat
    def clear_reservation(self):
        self.customer = None
        self.price = 0
    
    #Print seat status    
    def __str__(self):
        if self.customer:
            return f"Reserved for {self.customer} at price ${self.price}"
        return "Available"
