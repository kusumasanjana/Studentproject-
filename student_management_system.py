class Student:
    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, "
                f"Gender: {self.gender}, Average Grade: {self.get_average_grade():.2f}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, gender):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
            return False
        student = Student(student_id, name, age, gender)
        self.students[student_id] = student
        print(f"Student {name} added successfully.")
        return True

    def remove_student(self, student_id):
        if student_id not in self.students:
            print(f"No student found with ID {student_id}.")
            return False
        del self.students[student_id]
        print(f"Student with ID {student_id} removed successfully.")
        return True

    def add_grade(self, student_id, subject, grade):
        if student_id not in self.students:
            print(f"No student found with ID {student_id}.")
            return False
        self.students[student_id].add_grade(subject, grade)
        print(f"Grade added for student {student_id} in subject {subject}.")
        return True

    def get_student_info(self, student_id):
        if student_id not in self.students:
            print(f"No student found with ID {student_id}.")
            return None
        return str(self.students[student_id])

    def get_all_students(self):
        if not self.students:
            print("No students in the system.")
            return []
        return [str(student) for student in self.students.values()]

    def get_student_with_highest_grade(self):
        if not self.students:
            print("No students in the system.")
            return None
        best_student = max(self.students.values(), key=lambda s: s.get_average_grade())
        return str(best_student)


def main_menu():
    system = StudentManagementSystem()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Add Grade")
        print("4. Get Student Info")
        print("5. Get All Students")
        print("6. Get Student with Highest Grade")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender (M/F): ")
            system.add_student(student_id, name, age, gender)

        elif choice == '2':
            student_id = input("Enter student ID to remove: ")
            system.remove_student(student_id)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            system.add_grade(student_id, subject, grade)

        elif choice == '4':
            student_id = input("Enter student ID: ")
            info = system.get_student_info(student_id)
            if info:
                print("\n" + info)

        elif choice == '5':
            print("\n--- All Students ---")
            students = system.get_all_students()
            for student in students:
                print(student)

        elif choice == '6':
            print("\n--- Student with Highest Grade ---")
            best_student = system.get_student_with_highest_grade()
            if best_student:
                print(best_student)

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
