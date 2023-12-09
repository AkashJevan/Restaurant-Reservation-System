import tkinter as tk #import tkinter for gui
from gui import ReservationGUI #import class from gui file

#initialize & run reservation GUI
def main():
    root = tk.Tk()
    app = ReservationGUI(root)
    root.mainloop()

#only run when file is main
if __name__ == "__main__":
    main()
