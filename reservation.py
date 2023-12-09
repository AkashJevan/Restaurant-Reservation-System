class Reservation:
    #called when a new instance of Reservation is created
    def __init__(self, customer_name, reservation_date, reservation_time, party_size):
        self.customer_name = customer_name
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time
        self.party_size = party_size

    #converts the reservation details into a list
    def to_list(self):
        return [self.customer_name, self.reservation_date, self.reservation_time, self.party_size]

    #returns a formatted string
    def __str__(self):
        return (f"Reservation for {self.customer_name} on {self.reservation_date} "
                f"at {self.reservation_time} for {self.party_size} people.")
    
    #compare  reservations
    def __eq__(self, other):
        if isinstance(other, Reservation):
            return (self.customer_name == other.customer_name and 
                    self.reservation_date == other.reservation_date and
                    self.reservation_time == other.reservation_time and
                    self.party_size == other.party_size)
        return False
