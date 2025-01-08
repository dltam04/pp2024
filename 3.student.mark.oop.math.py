import math

# Student = [id, name, DoB]
# Course = [id, name,]
# nb = [Number of students/courses, etc.]
# stlst = [Student list, etc.]
# cslst = [Course list, etc.]

class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_dob = student_dob
        self.__student_gpa = 0.0

    def get_id(self):
        return self.__student_id
    
    def get_info(self):
        return {
            "id": self.__student_id,
            "name": self.__student_name,
            "dob": self.__student_dob,
            "gpa": self.__student_gpa
        }
    
    def get_gpa(self):
        return self.__student_gpa
    
    def set_gpa(self, student_gpa):
        self.__student_gpa = student_gpa

class Course:
    def __init__(self, course_id, course_name, course_credits):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_credits = course_credits
        self.__course_marks = {}

    def get_id(self):
        return self.__course_id
    
    def get_credits(self):
        return self.__course_credits

    def add_mark(self, student_id, mark):
        self.__course_marks[student_id] = mark

    def get_marks(self):
        return self.__course_marks

    def get_info(self):
        return {
            "id": self.__course_id,
            "credits": self.__course_credits,
            "name": self.__course_name,
            "marks": self.__course_marks
        }
    
class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_student(self):
        print("---")
        number_of_students = int(input("Number of students: "))
        for _ in range(number_of_students):
            student_id = input("Student ID: ")
            student_name = input("Student name: ")
            student_dob = input("Student DoB: ")
            self.__students.append(Student(student_name, student_id, student_dob))

    def input_course(self):
        print("---")
        number_of_courses = int(input("Number of courses: "))
        for _ in range(number_of_courses):
            course_id = input("Course ID: ")
            course_name = input("Course Name: ")
            course_credits = int(input("Course Credits: "))
            self.__courses.append(Course(course_id, course_name, course_credits))

    def list_students(self):
        print("---")
        for student in self.__students:
            info = student.get_info()
            print(f"ID: {info['id']}, Name: {info['name']}, DoB: {info['dob']}, GPA: {info['gpa']}")

    def list_courses(self):
        print("---")
        for course in self.__courses:
            info = course.get_info()
            print("---")
            print(f"Course ID: {info['id']}, Name: {info['name']}, Credits: {info['credits']}")
            print("+++")
            print("Marks:")
            for student_id, mark in info['marks'].items():
                print(f"Student {student_id}: {mark}")

    def list_marks(self):
        print("---")
        for course in self.__courses:
            info = course.get_info()
            print(f"Course ID: {info['id']}, Name: {info['name']}")
            print("+++")
            print("Marks:")
            for student_id, mark in info['marks'].items():
                print(f"Student {student_id}: {mark}")

    def add_mark(self):
        print("---")
        course_id = input("Enter Course ID: ")
        course = next((c for c in self.__courses if c.get_id() == course_id), None) 
        if not course:
            print("Course not found!")
            return

        for student in self.__students:
            i = student.get_id()
            mark = float(input(f"Enter mark for Student {i}: "))
            mark_int = math.floor(mark)
            course.add_mark(i, mark_int)

    def cal_gpa(self, student_id):
        print("---")
        total_credits = 0
        weighted_sum = 0

        for course in self.__courses:
            mark_to_cal = course.get_marks()
            if student_id in mark_to_cal:
                final_mark = mark_to_cal[student_id]
                credits = course.get_credits() 
                weighted_sum += final_mark * credits
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
                self.input_student()
            elif option == 2:
                self.input_course()
            elif option == 3:
                self.list_students()
            elif option == 4:
                self.list_courses()
            elif option == 5:
                self.add_mark()
            elif option == 6:
                self.list_marks()
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
    smm.menu()