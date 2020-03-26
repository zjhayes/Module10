import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student("Hayes", "Zachary", "CIS", 3.5)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, "Hayes")
        self.assertEqual(self.student.first_name, "Zachary")
        self.assertEqual(self.student.major, "CIS")
        self.assertEqual(self.student.gpa, 3.5)


if __name__ == '__main__':
    unittest.main()