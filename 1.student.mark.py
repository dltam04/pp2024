# Student = [id, name, DoB]
# Course = [id, name,]
# ... = [Number of students/courses, etc.]
# ... = [Student list, etc.]
# ... = [Course list, etc.]

def student_input(student_list):
    print("---")
    number_of_students = int(input("Number of students: "))
    for idx in range (number_of_students):
        print(f"Student number: {idx}")
        student_name = input ("Student name: ")
        student_id = input ("Student id: ")
        student_dob = input ("Student DoB: ")
        print("---")
        student_list.append([student_name, student_id, student_dob])

def course_input(course_list):
    print("---")
    number_of_courses = int(input("Number of courses: "))
    for idx in range (number_of_courses):
        print(f"Course number: {idx}")
        course_name = input ("Course name: ")
        course_id = input ("Course id: ")
        print("---")
        course_list.append([course_name, course_id, {}])

def mark_input(course_list, student_list):
    print("---")
    course_id = input("Select the course by course ID: ")
    course = [course for course in course_list if course[1] == course_id] [0]
    print("+++")
    print("Please insert student marks: ")
    for student in student_list:
        print("+++")
        mark = float(input(f"Student {student[1]} [{student[0]}] mark: "))
        course[2][student[0]] = mark
    print("---")

def list_students(student_list):
    print("---")
    print(f"There are {len(student_list)} students in system: ")
    for student in student_list:
        print("+++")
        print(f"Student name: {student[0]}")
        print(f"Student id: {student[1]}")
        print(f"Student DoB: {student[2]}")
    print("---")

def list_courses(course_list):
    print("---")
    print(f"There are {len(course_list)} courses in system: ")
    for course in course_list:
        print("+++")
        print(f"Course name: {course[0]}")
        print(f"Course id: {course[1]}")
        print(f"\nCourse marks: ")
        for k, v in course[2].items():
            print(f"Student [{k}] has mark: {v}")
    print("---")

if __name__ == "__main__":
    student_list = []
    course_list = []

    while True:
        opt = int(input(
                  
        """
        [Students mark management]
        1. Insert students.
        2. Insert courses.
        3. List students info.
        4. List courses info.
        5. Add mark.
        6. List mark.
        7. Exit.
        Opt:

        """))

        if opt == 1:
            student_input(student_list)
        elif opt == 2:
            course_input(course_list)
        elif opt == 3:
            list_students(student_list)
        elif opt == 4:
            list_courses(course_list)
        elif opt == 5:
            mark_input(course_list, student_list)
        elif opt == 6:
            list_courses(course_list)
        elif opt == 7:
            break
        else:
            print("Option not supported")