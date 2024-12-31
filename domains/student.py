class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__student_id
    
    def get_info(self):
        return {
            "id": self.__student_id,
            "name": self.__name,
            "dob": self.__dob,      
            "gpa": self.__gpa
        }
    
    def get_gpa(self):
        return self.__gpa  
    
    def set_gpa(self, gpa):
        self.__gpa = gpa