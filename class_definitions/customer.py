# Zachary Hayes
class Customer:
    '''Customer Class'''

    #Constructor
    def __init__(self, id, lname, fname, phone, add):

        if not isinstance(id, int):     # Constructor raises error.
            raise AttributeError        # Errors should be caught as early as possible.

        self.customer_id = id
        self.last_name = str(lname)
        self.first_name = str(fname)
        self.phone_number = str(phone)
        self.address = str(add)

    def set_customer_id(self, id):
        self.customer_id = id

    def display(self):
        return "Customer ID: " + str(self.customer_id) + "\n" + self.last_name + ", " + self.first_name + \
               "\nPhone: " + self.phone_number + "\n" + self.address
