class Student:

    def __init__(self, name, gender, datasheet, image_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.datasheet.get_grades_as_list()

        return sum(grades) / len(grades)

    def get_study_prog(self):
        sumects = 0

        for course in self.datasheet.courses:
            sumects += int(course.etcs)

        return sumects*2

    def get_courses(self):
        return self.datasheet.courses
