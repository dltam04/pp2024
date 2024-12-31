def input_st(self):
    print("---")
    nb = int(input("Number of students: "))
    for _ in range(nb):
        n = input("Student Name: ")
        i = input("Student ID: ")
        b = input("Student DoB: ")
        Student = []
        self.__students.append(Student(n, i, b))
    return Student    

def input_cs(self):
    print("---")
    nb = int(input("Number of courses: "))
    for _ in range(nb):
        i = input("Course ID: ")
        n = input("Course Name: ")
        cr = int(input("Course Credits: "))
        Course = []
        self.__courses.append(Course(i, n, cr))
    return Course