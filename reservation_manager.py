import csv
from reservation import Reservation

class ReservationManager:
    def __init__(self):
        self.reservations = []
        self.file_path = 'reservation.csv'
        self.load_from_file(self.file_path)

    def add_or_update_reservation(self, new_reservation):
        index_to_update = None
        for i, reservation in enumerate(self.reservations):
            if reservation.customer_name == new_reservation.customer_name and reservation.reservation_date == new_reservation.reservation_date:
                index_to_update = i
                break

        if index_to_update is not None:
            print("Updating existing reservation")
            self.reservations[index_to_update] = new_reservation
        else:
            print("Adding new reservation")
            self.reservations.append(new_reservation)

        self.save_to_file(self.file_path)

    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Date', 'Time', 'Party Size'])
                for reservation in self.reservations:
                    writer.writerow(reservation.to_list())
        except Exception as e:
            print(f"Error writing to file: {e}")

    def load_from_file(self, file_path):
        self.reservations.clear()
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                for row in reader:
                    if len(row) == 4:
                        row[3] = int(row[3])
                        reservation_obj = Reservation(*row)
                        self.reservations.append(reservation_obj)
        except FileNotFoundError:
            print(f"No existing file found at {file_path}, starting fresh.")
