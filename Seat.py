class Seat:
    #Constructor to initialize Seat object
    def __init__(self, date, time, party_size):
        self.customer = None
        self.date = date
        self.time = time
        self.party_size = party_size

    #Method to reserve a seat for a customer
    def reserve(self, customer):
        self.customer = customer

    #Method to clear a seat reservation
    def clear(self):
        self.customer = None

    #Method to return string representation of Seat object
    def __str__(self):
        if self.customer:
            return f"Seat reserved for {self.customer} on {self.date} at {self.time} for {self.party_size} people."
        else:
            return "Seat is available."
