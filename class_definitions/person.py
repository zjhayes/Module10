class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return self.last_name + ", " + self.first_name + " lives at " + self.address # This display is called