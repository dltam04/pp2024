# Student = [id, name, DoB]
# Course = [id, name,]
# nb = [Number of students/courses, etc.]
# stlst = [Student list, etc.]
# cslst = [Course list, etc.]

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__student_id
    
    def get_info(self):
        return {
            "id": self.__student_id,
            "name": self.__name,
            "dob": self.__dob
        }
    
class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name
        self.__marks = {}

    def get_id(self):
        return self.__course_id

    def add_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_marks(self):
        return self.__marks

    def get_info(self):
        return {
            "id": self.__course_id,
            "name": self.__name,
            "marks": self.__marks
        }
    
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
            self.__courses.append(Course(i, n))

    def stlst(self):
        print("---")
        for student in self.__students:
            info = student.get_info()
            print(f"ID: {info['id']}, Name: {info['name']}, DoB: {info['dob']}")

    def cslst(self):
        print("---")
        for course in self.__courses:
            info = course.get_info()
            print("---")
            print(f"Course ID: {info['id']}, Name: {info['name']}")
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
            course.add_mark(i, mrk)

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
                print("Exit.")
                break
            else:
                print("Option not supported.")


if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.menu()