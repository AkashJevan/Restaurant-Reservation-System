class Customer:
    #Constructor to initialize Customer object
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    #Method to return string representation of Customer object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"