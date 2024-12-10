import unittest
from myproject import StudentManagementSystem  # Import the class from myproject.py

class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        # Initialize the StudentManagementSystem object before each test
        self.system = StudentManagementSystem()

    def test_add_student(self):
        # Test that a student is added successfully
        result = self.system.add_student(1, "John Doe", 20, "Male")
        self.assertTrue(result)
        result = self.system.add_student(1, "Jane Doe", 22, "Female")
        self.assertFalse(result)  # Trying to add a student with the same ID should fail

    def test_add_grade(self):
        # Test that a grade is added successfully
        self.system.add_student(1, "John Doe", 20, "Male")
        result = self.system.add_grade(1, "Math", 85)  # Pass a numeric grade
        self.assertTrue(result)
        result = self.system.add_grade(1, "Math", "A")  # Pass a letter grade
        self.assertTrue(result)  # It should now work if letter grade conversion is implemented
        result = self.system.add_grade(1, "Math", "InvalidGrade")  # Pass an invalid grade
        self.assertFalse(result)

    def test_get_student_with_highest_grade(self):
        # Test that the student with the highest average grade is returned correctly
        self.system.add_student(1, "John Doe", 20, "Male")
        self.system.add_grade(1, "Math", 90)
        self.system.add_student(2, "Jane Doe", 22, "Female")
        self.system.add_grade(2, "Math", 95)

        best_student = self.system.get_student_with_highest_grade()
        self.assertIsNotNone(best_student)  # Ensure the best student is found
        self.assertEqual(best_student['name'], "Jane Doe")  # Check if the correct student is returned

    def test_get_student_info(self):
        # Test that student info is returned correctly
        self.system.add_student(1, "John Doe", 20, "Male")
        student_info = self.system.get_student_info(1)
        self.assertIn("John Doe", student_info)  # Check if the student name is part of the returned string

    
    def test_add_existing_student(self):
        student_id = "S001"
        name = "Alice"
        age = 20
        gender = "Female"
        # Add student for the first time
        self.system.add_student(student_id, name, age, gender)
        # Try adding the same student again (should fail)
        result = self.system.add_student(student_id, name, age, gender)
        self.assertFalse(result)  # Should return False since student already exists

    

    def test_add_invalid_grade(self):
        student_id = "S999"
        result = self.system.add_grade(student_id, "Math", "A")
        self.assertFalse(result)  # Student does not exist, should return False

    def test_remove_student(self):
        student_id = "S001"
        name = "Alice"
        age = 20
        gender = "Female"
        # Add student and then remove it
        self.system.add_student(student_id, name, age, gender)
        result = self.system.remove_student(student_id)
        self.assertTrue(result)  # Should be removed successfully

    def test_remove_non_existing_student(self):
        student_id = "S999"
        result = self.system.remove_student(student_id)
        self.assertFalse(result)  # No student with this ID, should return False

    

    def test_get_all_students(self):
        student_id_1 = "S001"
        student_id_2 = "S002"
        # Add multiple students
        self.system.add_student(student_id_1, "Alice", 20, "Female")
        self.system.add_student(student_id_2, "Bob", 22, "Male")
        all_students = self.system.get_all_students()
        self.assertEqual(len(all_students), 2)  # Check if both students are present

    def test_get_student_with_highest_grade(self):
        student_id_1 = "S001"
        student_id_2 = "S002"
        # Add students and grades
        self.system.add_student(student_id_1, "Alice", 20, "Female")
        self.system.add_student(student_id_2, "Bob", 22, "Male")
        self.system.add_grade(student_id_1, "Math", "A")
        self.system.add_grade(student_id_2, "Math", "B")
        best_student = self.system.get_student_with_highest_grade("Math")
        self.assertEqual(best_student['name'], "Alice")  # Alice has the highest grade in Math

if __name__ == '__main__':
    unittest.main()

