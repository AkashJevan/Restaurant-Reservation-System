from Seat import Seat
from Customer import Customer

def main():
    #Take input
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    date = input("Enter the date of reservation (YYYY-MM-DD): ")
    time = input("Enter the time of reservation (HH:MM): ")
    party_size = int(input("Enter the party size: "))

    #Create customer and seat
    customer = Customer(first_name, last_name)
    seat_A1 = Seat(date, time, party_size)

    #Reserve seat for customer
    seat_A1.reserve(customer)

    #Print output
    print(seat_A1)

if __name__ == "__main__":
    main()