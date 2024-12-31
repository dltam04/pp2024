class Course:
    def __init__(self, course_id, name, credits):
        self.__course_id = course_id
        self.__name = name
        self.__credits = credits
        self.__marks = {}

    def get_id(self):
        return self.__course_id
    
    def get_credits(self):
        return self.__credits

    def add_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_marks(self):
        return self.__marks

    def get_info(self):
        return {
            "id": self.__course_id,
            "credits": self.__credits,
            "name": self.__name,
            "marks": self.__marks
        }