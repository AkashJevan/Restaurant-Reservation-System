import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from reservation import Reservation
from reservation_manager import ReservationManager

class ReservationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Restaurant Reservation System")

        # Initialize the reservation manager
        self.reservation_manager = ReservationManager()

        # Create and place the labels and entry widgets for the form
        self.label_name = tk.Label(master, text="Name")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_date = tk.Label(master, text="Date (MM-DD)")
        self.label_date.grid(row=1, column=0)
        self.entry_date = tk.Entry(master)
        self.entry_date.grid(row=1, column=1)

        self.label_time = tk.Label(master, text="Time (HH:MM)")
        self.label_time.grid(row=2, column=0)
        self.entry_time = tk.Entry(master)
        self.entry_time.grid(row=2, column=1)

        self.label_party_size = tk.Label(master, text="Party Size")
        self.label_party_size.grid(row=3, column=0)
        self.entry_party_size = tk.Entry(master)
        self.entry_party_size.grid(row=3, column=1)

        # Create and place the submit button
        self.submit_button = tk.Button(master, text="Submit Reservation", command=self.submit)
        self.submit_button.grid(row=4, column=0, columnspan=2)

    def submit(self):
        # Get the values from the entries
        name = self.entry_name.get()
        date = self.entry_date.get()
        time = self.entry_time.get()
        party_size = self.entry_party_size.get()

        # Validate and create reservation
        if self.validate_date(date) and self.validate_time(time) and name and party_size.isdigit():
            reservation = Reservation(name, date, time, int(party_size))
            self.reservation_manager.add_reservation(reservation)
            self.reservation_manager.save_to_file('reservations.txt')
            messagebox.showinfo("Reservation Submitted", "Reservation has been successfully submitted!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter valid reservation details.")

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%m-%d')
            return True
        except ValueError:
            return False

    def validate_time(self, time_text):
        try:
            datetime.strptime(time_text, '%H:%M')
            return True
        except ValueError:
            return False

    def clear_entries(self):
        # Clear the entry fields for a new reservation
        self.entry_name.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_party_size.delete(0, tk.END)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    gui = ReservationGUI(root)
    root.mainloop()
