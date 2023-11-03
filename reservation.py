class Reservation:
    def __init__(self, customer_name, reservation_date, reservation_time, party_size):
        self.customer_name = customer_name
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time
        self.party_size = party_size

    def __str__(self):
        return (f"Reservation for {self.customer_name} on {self.reservation_date} "
                f"at {self.reservation_time} for {self.party_size} people.")
