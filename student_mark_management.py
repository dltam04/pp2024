from domains import Student, Course

import input
import output
import math

class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_st(self):
        print("---")
        nb = int(input("Number of students: "))
        for _ in range(nb):
            n = input("Student Name: ")
            i = input("Student ID: ")
            b = input("Student DoB: ")
            self.__students.append(Student(n, i, b))

    def input_cs(self):
        print("---")
        nb = int(input("Number of courses: "))
        for _ in range(nb):
            i = input("Course ID: ")
            n = input("Course Name: ")
            cr = int(input("Course Credits: "))
            self.__courses.append(Course(i, n, cr))

    def stlst(self):
        print("---")
        for student in self.__students:
            info = student.get_info()
            print(f"ID: {info['id']}, Name: {info['name']}, DoB: {info['dob']}, GPA: {info['gpa']}")

    def cslst(self):
        print("---")
        for course in self.__courses:
            info = course.get_info()
            print("---")
            print(f"Course ID: {info['id']}, Name: {info['name']}, Credits: {info['credits']}")
            print("+++")
            print("Marks:")
            for student_id, mrk in info['marks'].items():
                print(f"Student {student_id}: {mrk}")

    def mrklst(self):
        print("---")
        for course in self.__courses:
            info = course.get_info()
            print(f"Course ID: {info['id']}, Name: {info['name']}")
            print("+++")
            print("Marks:")
            for student_id, mrk in info['marks'].items():
                print(f"Student {student_id}: {mrk}")

    def add_mark(self):
        print("---")
        course_id = input("Enter Course ID: ")
        course = next((c for c in self.__courses if c.get_id() == course_id), None)
        if not course:
            print("Course not found!")
            return

        for student in self.__students:
            i = student.get_id()
            mrk = float(input(f"Enter mark for Student {i}: "))
            result = math.floor(mrk)
            course.add_mark(i, result)

def cal_gpa(self, student_id):
        print("---")
        total_credits = 0
        weighted_sum = 0

        for course in self.__courses:
            marks = course.get_marks()
            if student_id in marks:
                mark = marks[student_id]
                credits = course.get_credits() 
                weighted_sum += mark * credits
                total_credits += credits

        return round(weighted_sum / total_credits, 2) if total_credits > 0 else 0.0
    
def calculate_gpa(self):
    for student in self.__students:
        gpa = self.cal_gpa(student.get_id())
        student.set_gpa(gpa)

    print("Updated GPAs:")
    for student in self.__students:
        info = student.get_info()
        print(f"ID: {info['id']}, Name: {['name']}, GPA: {info['gpa']}")

def sort_by_gpa(self):
    self.__students.sort(key = lambda s: s.get_gpa(), reverse = True)
    print("---")
    print("Students sorted by GPA (descending):")
    for student in self.__students:
        info = student.get_info()
        print(f"ID: {info['id']}, Name: {info['name']}, GPA: {info['gpa']}")

def menu(self):
    while True:
        print("\n[Student Mark Management System]")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Add marks")
        print("6. List marks")
        print("7. Calculate GPA")
        print("8. Sort students by GPA")
        print("9. Exit")

        option = int(input("Select an option: "))
        if option == 1:
            self.input_st()
        elif option == 2:
            self.input_cs()
        elif option == 3:
            self.stlst()
        elif option == 4:
            self.cslst()
        elif option == 5:
            self.add_mark()
        elif option == 6:
            self.mrklst()
        elif option == 7:
            self.calculate_gpa()
            print("GPA calculated for all students.")
        elif option == 8:
            self.sort_by_gpa()
            print("Students sorted by GPA.")
        elif option == 9:
            print("Exit.")
            break
        else:
            print("Option not supported.")

if __name__ == "__main__":
    smm = StudentMarkManagement()