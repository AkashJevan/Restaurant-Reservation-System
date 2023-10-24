import tkinter as tk
from Seat import Seat
from Customer import Customer

class Reservation:
    def __init__(self, root):
        self.root = root
        self.root.title("Table Reservation")

        #Define a list of questions and their corresponding validation functions
        self.questions = [
            ("First Name:", self.validate_name_input),
            ("Last Name:", self.validate_name_input),
            ("Date (YYYY-MM-DD):", self.validate_date),
            ("Time (HH:MM):", self.validate_time),
            ("Party Size (1-10):", self.validate_party_size)
        ]

        #Create StringVar variables to store user answers
        self.answers = [tk.StringVar() for _ in self.questions]

        #Initialize the current question index
        self.current_question = 0

        #Create and display the label for the current question
        self.label_question = tk.Label(root, text=self.questions[self.current_question][0])
        self.label_question.pack()

        #Create an entry field for the user's answer to the current question
        self.entry_answer = tk.Entry(root, textvariable=self.answers[self.current_question])
        self.entry_answer.pack()

        #Create the "Next" button to move to the next question
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack()

        #Create the "Reserve" button (initially invisible)
        self.reserve_button = tk.Button(root, text="Reserve", command=self.reserve_table)
        self.reserve_button.pack()
        self.reserve_button.pack_forget()

        #Create a label for error messages (initially invisible)
        self.label_error = tk.Label(root, text="", fg="red")
        self.label_error.pack()
        self.label_error.pack_forget()

    def next_question(self):
        #Clear any existing error message
        self.label_error.pack_forget()

        #Get the current question and its validation function
        current_question, validation_function = self.questions[self.current_question]

        #Get the user's answer
        user_answer = self.answers[self.current_question].get()

        #If there is a validation function and it returns True or there's no validation function, proceed
        if not validation_function or (validation_function and validation_function(user_answer)):
            if self.current_question < len(self.questions) - 1:
                #Move to the next question
                self.current_question += 1

                #Clear the entry field for the current question
                self.entry_answer.delete(0, tk.END)

                #Update the label with the next question
                self.label_question.config(text=self.questions[self.current_question][0])

                #If it's the last question, show the "Reserve" button
                if self.current_question == len(self.questions) - 1:
                    self.next_button.pack_forget()
                    self.reserve_button.pack()
            else:
                #If all questions are answered, show the "Reserve" button
                self.next_button.pack_forget()
                self.reserve_button.pack()
        else:
            #Display an error message for incorrect input
            self.label_error.config(text=f"Invalid input for {current_question}")
            self.label_error.pack()

    def reserve_table(self):
        #Clear any existing error message
        self.label_error.pack_forget()

        #Get user answers
        first_name = self.answers[0].get()
        last_name = self.answers[1].get()
        date = self.answers[2].get()
        time = self.answers[3].get()
        party_size = self.answers[4].get()

        try:
            #Convert party size to integer
            party_size = int(party_size)

            #Check party size constraints
            if 1 <= party_size <= 10:
                #Create a customer and seat
                customer = Customer(first_name, last_name)
                seat_A1 = Seat(date, time, party_size)

                #Reserve seat for customer
                seat_A1.reserve(customer)

                #Print reservation details
                reservation_details = f"Reserved for {customer} on {date} at {time} for {party_size} people."
                print(reservation_details)

                #Clear user entries
                self.clear_entries()
            else:
                #Print error message if party size is out of bounds
                print("Invalid party size. Must be between 1 and 10.")
                self.label_error.config(text="Invalid party size. Must be between 1 and 10.")
                self.label_error.pack()

        except ValueError:
            #Print error message if input values are invalid
            print("Invalid input values. Please enter valid numbers.")
            self.label_error.config(text="Invalid input values. Please enter valid numbers.")
            self.label_error.pack()

    def clear_entries(self):
        #Clear user entries
        for entry in self.answers:
            entry.set("")

    #Validation functions
    def validate_name_input(self, input_str):
        #Validate that the input string consists only of alphabets and spaces
        return input_str.replace(" ", "").isalpha()

    def validate_any_input(self, input_str):
        return bool(input_str.strip())

    def validate_date(self, date_str):
        parts = date_str.split("-")
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            year, month, day = map(int, parts)
            return 1 <= month <= 12 and 1 <= day <= 31 and year > 0
        return False

    def validate_time(self, time_str):
        parts = time_str.split(":")
        if len(parts) == 2 and all(part.isdigit() for part in parts):
            hour, minute = map(int, parts)
            return 0 <= hour <= 23 and 0 <= minute <= 59
        return False

    def validate_party_size(self, size_str):
        if size_str.isdigit():
            size = int(size_str)
            return 1 <= size <= 10
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = Reservation(root)
    root.mainloop()
