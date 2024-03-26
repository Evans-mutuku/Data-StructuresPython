# Question
""" Suppose we are managing a database of student records and need to store information such as student ID, name, age, and GPA. How can we use a linked list to efficiently organize and manage this data? """



class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
        self.next = None

class StudentDatabase:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, age, gpa):
        new_student = Student(student_id, name, age, gpa)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

    def display_students(self):
        current = self.head
        while current:
            print(f"Student ID: {current.student_id}, Name: {current.name}, Age: {current.age}, GPA: {current.gpa}")
            current = current.next

# Example Usage:
student_db = StudentDatabase()
student_db.add_student(101, "Alice", 20, 3.5)
student_db.add_student(102, "Bob", 21, 3.8)
student_db.add_student(103, "Charlie", 19, 3.2)
student_db.display_students()
