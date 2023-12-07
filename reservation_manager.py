import csv
from reservation import Reservation

class ReservationManager:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def save_to_file(self, file_path):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            for reservation in self.reservations:
                writer.writerow(reservation.to_list())
                
    def load_from_file(self, file_path):
        self.reservations = []  # Clear existing reservations
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                header = next(reader)  # Skip the header row
                for row in reader:
                    # Assuming the row contains [name, date, time, party_size]
                    customer_name, reservation_date, reservation_time, party_size = map(str.strip, row)
                    reservation_obj = Reservation(customer_name, reservation_date, reservation_time, int(party_size))
                    self.add_reservation(reservation_obj)
                return [str(reservation) for reservation in self.reservations]  # Ensure correct data is returned

        except FileNotFoundError:
            # Handle the case where the file does not exist
            pass
        return []
