#students = []


class Student:
    school_name = "Parish church"

    def __init__(self, name, student_id=332): # constructor?
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "Parish Church Junior"

    def get_school_name(self):
        return "This is Junior student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-JSCHOOL"

Peter = Student("Peter")
Rex = Student("Rex")

print(Peter)
print(Rex)

print(Peter.get_name_capitalize())
print(Rex.get_name_capitalize())

print(Student.school_name)

print(HighSchoolStudent.school_name)

James = HighSchoolStudent("james")
print(James.get_name_capitalize())
