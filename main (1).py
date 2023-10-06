
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def short_Student(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("John", "A101", 3.8)
student2 = Student("Alice", "A102", 3.5)
student3 = Student("Bob", "A103", 3.9)

students = [student1, student2, student3]

sorted_students = short_Student(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
