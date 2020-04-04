from class_definitions.employee import Employee
import datetime


class SalariedEmployee(Employee):
    '''SalariedEmployee class'''

    # Constructor
    def __init__(self, lname, fname, add, phone, sdate, sal):
        super().__init__(lname, fname, add, phone)
        self.start_date = sdate
        self.salary = sal

    def give_raise(self, amt):
        self.salary += amt

    def display(self):
        return self.last_name + ", " + self.first_name + "\n" + self.address + "\nPhone: " + self.phone_number + \
               "\nStart Date: " + str(self.start_date) + "\nSalary: $%.2f" % self.salary


# Driver
new_salaried = SalariedEmployee("Hayes", "Zachary", "123 Fake Street", "515-555-5555", datetime.date.today(), 40000)
print(new_salaried.display())
new_salaried.give_raise(5000)
print(new_salaried.display())
del new_salaried
