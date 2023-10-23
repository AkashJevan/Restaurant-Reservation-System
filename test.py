#GUI 
import tkinter as tk

#Defining seat n properties 
class Seat:
    #Setting viod seat
    def __init__(self):
        self.user = None
        self.price = 0

    #Reserve user n price for seat
    def reserve(self, user, price):
        self.user = user
        self.price = price

    #Emty seat
    def clear_reservation(self):
        self.user = None
        self.price = 0

    #Print seat status
    def __str__(self):
        if self.user:
            return f"Reserved for {self.user} at price ${self.price}"
        return "Available"

#Setting User info
class User:
    #Initializing user info
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    #Make into string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

def main():
    #Take input
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")

    #Create user and seat
    user = User(first_name, last_name)
    seat_A1 = Seat()

    #Reserve seat for user
    seat_A1.reserve(user, 100)

    #Print output
    print(seat_A1)

#Call main
if __name__ == "__main__":
    main()

