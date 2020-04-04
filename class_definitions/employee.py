class Employee:
    '''Employee Class '''

    # Constructor
    def __init__(self, lname, fname, add, phone):
        self.last_name = lname
        self.first_name = fname
        self.address = add
        self.phone_number = phone

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, add):
        self.address = add

    def set_phone_number(self, phone):
        self.phone_number = phone
