from class_definitions.employee import Employee
import datetime


class HourlyEmployee(Employee):
    '''HourlyEmployee class'''

    # Constructor
    def __init__(self, lname, fname, add, phone, sdate, pay):
        super().__init__(lname, fname, add, phone)
        self.start_date = sdate
        self.hourly_pay = pay

    def give_raise(self, amt):
        self.hourly_pay += amt

    def display(self):
        return self.last_name + ", " + self.first_name + "\n" + self.address + "\nPhone: " + self.phone_number + \
               "\nStart Date: " + str(self.start_date) + "\nHourly Pay: $%.2f" % self.hourly_pay


# Driver
new_hourly = HourlyEmployee("Hayes", "Zachary", "123 Fake Street", "515-555-5555", datetime.date.today(), 10.00)
print(new_hourly.display())
new_hourly.give_raise(2.00)
print(new_hourly.display())
del new_hourly
