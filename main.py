import tkinter as tk
from gui import ReservationGUI

def main():
    root = tk.Tk()
    app = ReservationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
