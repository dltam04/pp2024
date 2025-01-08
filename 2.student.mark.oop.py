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

    def get_id(self):
        return self.__student_id
    
    def get_info(self):
        return {
            "id": self.__student_id,
            "name": self.__student_name,
            "dob": self.__student_dob
        }
    
class Course:
    def __init__(self, course_name, course_id):
        self.__course_name = course_name
        self.__course_id = course_id
        self.__marks = {}

    def get_id(self):
        return self.__course_id

    def add_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_marks(self):
        return self.__marks

    def get_info(self):
        return {
            "id": self.__course_name,
            "name": self.__course_id,
            "marks": self.__marks
        }
    
class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_student(self):
        print("---")
        number_of_students = int(input("Number of students: "))
        for _ in range(number_of_students):
            student_name = input("Student Name: ")
            student_id = input("Student ID: ")
            student_dob = input("Student DoB: ")
            self.__students.append(Student(student_name, student_id, student_dob))

    def input_course(self):
        print("---")
        number_of_courses = int(input("Number of courses: "))
        for _ in range(number_of_courses):
            course_name = input("Course name: ")
            course_id = input("Course id: ")
            self.__courses.append(Course(course_name, course_id))

    def sudent_list(self):
        print("---")
        for student in self.__students:
            info = student.get_info()
            print(f"ID: {info['id']}, Name: {info['name']}, DoB: {info['dob']}")

    def course_list(self):
        print("---")
        for course in self.__courses:
            info = course.get_info()
            print("---")
            print(f"Course ID: {info['id']}, Name: {info['name']}")
            print("+++")
            print("Marks:")
            for student_id, mark in info['marks'].items():
                print(f"Student {student_id}: {mark}")

    def mark_list(self):
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
            course.add_mark(i, mark)

    def menu(self):
        while True:
            print("\n[Student Mark Management System]")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Add marks")
            print("6. List marks")
            print("7. Exit")

            opt = int(input("Select an option: "))
            if opt == 1:
                self.input_student()
            elif opt == 2:
                self.input_course()
            elif opt == 3:
                self.student_list()
            elif opt == 4:
                self.course_list()
            elif opt == 5:
                self.add_mark()
            elif opt == 6:
                self.mark_list()
            elif opt == 7:
                print("Exit.")
                break
            else:
                print("Option not supported.")


if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.menu()