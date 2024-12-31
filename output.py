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
