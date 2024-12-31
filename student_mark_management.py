from domains.student import Student # type: ignore
from domains.course import Course # type: ignore

import input # type: ignore
import output # type: ignore
import math
import zipfile
import os

class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
        self.load_data()

    def input_st(self):
        print("---")
        nb = int(input("Number of students: "))
        for _ in range(nb):
            n = input("Student Name: ")
            i = input("Student ID: ")
            b = input("Student DoB: ")
            student = Student(n, i, b)
            self.__students.append(student)

        # Write student into a .txt file 
        with open("students.txt", "w") as f:
            for _ in self.__students:
                f.write(f"{student.get_id()},{student.get_name()},{student.get_dob()}\n")
        print("Student data saved to students.txt")

    def input_cs(self):
        print("---")
        nb = int(input("Number of courses: "))
        for _ in range(nb):
            i = input("Course ID: ")
            n = input("Course Name: ")
            cr = int(input("Course Credits: "))
            course = Course(i, n, cr)
            self.__courses.append(Course)

        # Write course info to file
        with open("courses.txt", "w") as f:
            for course in self.__courses:
                f.write(f"{course.get_id()},{course.get_name()},{course.get_credits()}\n")
        print("Course data saved to courses.txt")

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
            mrks = math.floor(mrk)
            course.add_mark(i, mrks)

         # Write marks to file
        with open("marks.txt", "w") as f:
            for course_id, mrks in self.__marks.items():
                for student_id, mark in mrks.items():
                    f.write(f"{course_id},{student_id},{mark}\n")
        print("Marks data saved to marks.txt")

    def cal_gpa(self, student_id):
            print("---")
            total_credits = 0
            weighted_sum = 0

            for course in self.__courses:
                mrks = course.add_marks()
                if student_id in mrks:
                    mark = mrks[student_id]
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

    def compress_files(self):
            """Compress the generated files into a 'students.dat'."""
            compression_choice = input("Choose compression method (1 for ZIP_DEFLATED, 2 for no compression): ")

            if compression_choice == "1":
                compression = zipfile.ZIP_DEFLATED
            elif compression_choice == "2":
                compression = zipfile.ZIP_STORED
            else:
                print("Invalid choice. Defaulting to no compression.")
                compression = zipfile.ZIP_STORED

            # Compress the files
            with zipfile.ZipFile("students.dat", "w", compression) as zipf:
                zipf.write("students.txt")
                zipf.write("courses.txt")
                zipf.write("marks.txt")

            print("Files have been compressed into 'students.dat'.")

    def load_data(self):
        """Check for 'students.dat', decompress it, and load the data."""
        if os.path.exists("students.dat"):
            print("Found 'students.dat'. Decompressing and loading data...")
            with zipfile.ZipFile("students.dat", "r") as zipf:
                zipf.extractall()  # Extract all files from the archive

            # Load data from the extracted files
            self.__students = self.read_students()
            self.__courses = self.read_courses()
            self.__marks = self.read_marks()
            print("Data loaded successfully.")
        else:
            print("'students.dat' not found. Starting with empty data.")

    def read_students(self):
        """Read student data from 'students.txt'."""
        students = []
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                for line in f:
                    student_id, name, dob = line.strip().split(",")
                    students.append(Student(student_id, name, dob))
        return students

    def read_courses(self):
        """Read course data from 'courses.txt'."""
        courses = []
        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as f:
                for line in f:
                    course_id, name, credits = line.strip().split(",")
                    courses.append(Course(course_id, name, int(credits)))
        return courses

    def read_marks(self):
        """Read marks data from 'marks.txt'."""
        marks = {}
        if os.path.exists("marks.txt"):
            with open("marks.txt", "r") as f:
                for line in f:
                    course_id, student_id, mark = line.strip().split(",")
                    if course_id not in marks:
                        marks[course_id] = {}
                    marks[course_id][student_id] = float(mark)
        return marks

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
            print("9. Compress file and exit")

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
                self.compress_files()
                print("Exiting programs.")
                break
            else:
                print("Option not supported.")

if __name__ == "__main__":
    smm = StudentMarkManagement()