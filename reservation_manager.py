class ReservationManager:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write("Name\tDate\tTime\tParty Size\n")
            for reservation in self.reservations:
                file.write(f"{reservation.customer_name}\t{reservation.reservation_date}\t"
                           f"{reservation.reservation_time}\t{reservation.party_size}\n")
