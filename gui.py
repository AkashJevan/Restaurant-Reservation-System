import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from reservation import Reservation
from reservation_manager import ReservationManager

class ReservationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Restaurant Reservation System")
        self.reservation_manager = ReservationManager()
        self.setup_widgets()

    def setup_widgets(self):
        # UI layout
        self.label_name = tk.Label(self.master, text="Name")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1)

        self.label_date = tk.Label(self.master, text="Date (MM-DD)")
        self.label_date.grid(row=1, column=0)
        self.entry_date = tk.Entry(self.master)
        self.entry_date.grid(row=1, column=1)

        self.label_time = tk.Label(self.master, text="Time (HH:MM)")
        self.label_time.grid(row=2, column=0)
        self.entry_time = tk.Entry(self.master)
        self.entry_time.grid(row=2, column=1)

        self.label_party_size = tk.Label(self.master, text="Party Size")
        self.label_party_size.grid(row=3, column=0)
        self.entry_party_size = tk.Entry(self.master)
        self.entry_party_size.grid(row=3, column=1)

        self.label_reservation = tk.Label(self.master, text="Select Reservation")
        self.label_reservation.grid(row=4, column=0)
        self.reservation_var = tk.StringVar()
        self.reservation_dropdown = ttk.Combobox(self.master, textvariable=self.reservation_var, state="readonly")
        self.reservation_dropdown.grid(row=4, column=1)
        self.reservation_dropdown.bind("<<ComboboxSelected>>", self.show_selected_reservation)

        self.submit_button = tk.Button(self.master, text="Submit Reservation", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=2)

        self.load_reservations()

    def submit(self):
        name = self.entry_name.get()
        date = self.entry_date.get()
        time = self.entry_time.get()
        party_size = self.entry_party_size.get()

        if self.validate_date(date) and self.validate_time(time) and name and party_size.isdigit():
            reservation = Reservation(name, date, time, int(party_size))
            # Update the line below to use add_or_update_reservation
            self.reservation_manager.add_or_update_reservation(reservation)
            messagebox.showinfo("Reservation Submitted", "Reservation has been successfully submitted!")
            self.clear_entries()
            self.load_reservations()
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
        self.entry_name.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_party_size.delete(0, tk.END)

    def load_reservations(self):
        self.reservation_manager.load_from_file('reservation.csv')
        reservation_names = [r.customer_name for r in self.reservation_manager.reservations]
        self.reservation_dropdown['values'] = reservation_names

    def show_selected_reservation(self, event=None):
        selected_name = self.reservation_var.get()

        for reservation in self.reservation_manager.reservations:
            if reservation.customer_name == selected_name:
                details = f"Name: {reservation.customer_name}\n" \
                        f"Date: {reservation.reservation_date}\n" \
                        f"Time: {reservation.reservation_time}\n" \
                        f"Party Size: {reservation.party_size}"
                messagebox.showinfo("Reservation Details", details)
                return  # Exit the loop once the match is found

        messagebox.showerror("Error", "Selected reservation not found!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ReservationGUI(root)
    root.mainloop()
