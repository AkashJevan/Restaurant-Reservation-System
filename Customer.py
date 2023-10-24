#Setting Customer info
class Customer:
    #Initializing customer info
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

     #Make into string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"