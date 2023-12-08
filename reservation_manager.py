import csv
from reservation import Reservation

class ReservationManager:
    def __init__(self):
        self.reservations = []
        self.file_path = 'reservation.csv'  # Consistent file name
        self.load_from_file(self.file_path)

    def add_reservation(self, reservation):
        if not any(r.customer_name == reservation.customer_name and r.reservation_date == reservation.reservation_date for r in self.reservations):
            self.reservations.append(reservation)
            self.save_to_file(self.file_path)

    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w', newline='') as file:  # Overwrite mode
                writer = csv.writer(file)
                writer.writerow(['Name', 'Date', 'Time', 'Party Size'])
                for reservation in self.reservations:
                    writer.writerow(reservation.to_list())
            print("File written successfully")
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
                        row[3] = int(row[3])  # Convert party size to integer
                        reservation_obj = Reservation(*row)
                        self.reservations.append(reservation_obj)
        except FileNotFoundError:
            print(f"No existing file found at {file_path}, starting fresh.")
