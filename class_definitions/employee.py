import datetime

class Employee:
    '''Employee Class '''

    # Constructor
    def __init__(self, lname, fname, add, phone, sald, start, sal):
        self.last_name = lname
        self.first_name = fname
        self.address = add
        self.phone_number = phone
        self.salaried = sald
        self.start_date = start
        self.salary = sal

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, add):
        self.address = add

    def set_phone_number(self, phone):
        self.phone_number = phone

    def set_salaried(self, sald):
        self.salaried = sald

    def set_start_date(self, start):
        self.start_date = start

    def set_salary(self, sal):
        self.salary = sal

    def display(self):
        if(self.salaried):
            salary_display = "\nSalaried employee: $%.2f/year" % self.salary
        else:
            salary_display = "\nNot salaried"

        start_date_display = "\nStart date: " + str(self.start_date.date())

        return str(self.first_name) + " " + str(self.last_name) + "\n" + str(self.address) + salary_display + start_date_display


# Driver
emp = Employee("Ruiz", "Matthew", "123 Main Street\nUrban, Iowa", "555-123-4567", True, datetime.datetime(2020, 5, 17), 50000.00)   # call the construtor, needs to have a first and last name in parameter
emp.set_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
del emp                             # clean up!