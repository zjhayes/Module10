from class_definitions.person import Person


class Student(Person):
    """Student class"""
    def __init__(self, ident, lname, fname, major="General", gpa=0.0):
        super().__init__(lname, fname)
        if 0.0 > float(gpa) > 4.0 or not isinstance(gpa, float):
            raise ValueError
        self.id = ident
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.person.last_name + ", " + self.person.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        if 0.0 > float(new_gpa) > 4.0 or not isinstance(new_gpa, float):
            raise ValueError
        self.gpa = new_gpa

    def display(self):
        return self.last_name + ", " + self.first_name + "(" + str(self.id) + ") " + self.major + " gpa:" + str(self.gpa)


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student

