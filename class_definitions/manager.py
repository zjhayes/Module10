from class_definitions.person import Person
from class_definitions.salaried_employee import SalariedEmployee
import datetime


class Manager(Person, SalariedEmployee):
    '''Manager class'''

    # Constructor
    def __init__(self, lname, fname, add, phone, sdate, sal, dept):
        Person.__init__(self, lname, fname, add)
        SalariedEmployee.__init__(self, lname, fname, add, phone, sdate, sal)
        self.department = dept
        self.direct_reports = [SalariedEmployee("Smith", "John", "321 Main Street", "515-555-5555",
                                                datetime.date.today(), 30000),
                               SalariedEmployee("Doe", "Jane", "246 Maple Street", "515-555-5555",
                                                datetime.date.today(), 35000)]


# Driver
new_manager = Manager("Hayes", "Zachary", "123 Fake Street", "515-555-5555", datetime.date.today(), 40000, "IT")
print(new_manager.display())
print("Report:")
for report in new_manager.direct_reports:
    print(report.display())
new_manager.give_raise(2000)
print(new_manager.display())
del new_manager
