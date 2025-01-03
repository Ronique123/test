class Student:
    def add_student(self):
        name = input("Enter name of student: ")
        print(f"The name of the student is {name}")
     
    def student_address(self):
        address = input("Enter address of the student: ")
        print(f"The addressof the student is {address}")

    def student_number(self):
        number = input("Enter number of student: ")
        print(f"The number of student is {number} ")
 
student=Student()
student.add_student()
student.student_address()
student.student_number()