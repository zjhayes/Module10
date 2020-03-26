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

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, "Hayes")
        self.assertEqual(self.student.first_name, "Zachary")
        self.assertEqual(self.student.major, "CIS")
        self.assertEqual(self.student.gpa, 3.5)

    def test_student_str(self):
        self.assertEqual(str(self.student), "Hayes, Zachary has major CIS with gpa 3.5")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = t.Student("123", "Zachary", "CIS", 3.5)

    def test_object_not_created_first_name(self):
        with self.assertRaises(ValueError):
            s = t.Student("Hayes", "123", "CIS", 3.5)


if __name__ == '__main__':
    unittest.main()
