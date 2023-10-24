import tkinter as tk
from tkinter import messagebox

class ReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation Program")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.date_label = tk.Label(root, text="Date:")
        self.date_label.pack()

        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.time_label = tk.Label(root, text="Time:")
        self.time_label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.reserve_button = tk.Button(root, text="Reserve", command=self.make_reservation)
        self.reserve_button.pack()

    def make_reservation(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if name and date and time:
            # You can implement the reservation logic here, e.g., save to a database.
            # For this example, we'll display a message box.
            reservation_info = f"Name: {name}\nDate: {date}\nTime: {time}"
            messagebox.showinfo("Reservation Confirmation", f"Reservation Details:\n{reservation_info}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationApp(root)
    root.mainloop()