from Seat import Seat
from Customer import Customer

#Take input
def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")

    #Create customer and seat
    customer = Customer(first_name, last_name)
    seat_A1 = Seat()

    #Reserve seat for customer
    seat_A1.reserve(customer, 100)
    
    #Print output
    print(seat_A1)

if __name__ == "__main__":
    main()
