import student
import dataSheet
import course
import random
import csv

subjects = ["Math", "English", "Comp.Sci.", "Biology", "History"]

classrooms = ["1a", "1b", "1c", "2a", "2b"]

teachernames = ["Kurt", "Line", "Svend", "Luna", "Lotte"]

studentnames = ["Kristian", "Ahmed", "Kamilla", "Rasmus", "Sarah"]

genders = ["Male", "Male", "Female", "Male", "Female"]


def generate():
    students = []

    for i in range(5):
        course1 = course.Course(subjects[random.randint(0, 4)], classrooms[random.randint(0, 4)],
                                teachernames[random.randint(0, 4)], random.randint(20, 40), random.randint(0, 10))

        course2 = course.Course(subjects[random.randint(0, 4)], classrooms[random.randint(0, 4)],
                                teachernames[random.randint(0, 4)], random.randint(20, 40), random.randint(0, 10))

        students.append(
            student.Student(studentnames[i], genders[i], dataSheet.DataSheet(course1, course2), "Image: " + str(i)))

    with open("output.csv", "w") as f:
        csvwriter = csv.writer(f, delimiter=';')

        csvwriter.writerow(["stud_name", "course_name", "teacher", "gender", "etcs", "classroom", "grade", "img_url"])

        for stu in students:
            for cour in stu.datasheet.courses:
                csvwriter.writerow(
                    [stu.name, cour.name, cour.teacher, stu.gender, cour.etcs, cour.classroom, cour.grade,
                     stu.image_url])


def read_from_csv():
    students = []

    with open("output.csv", "r") as f:
        csvreader = csv.reader(f, delimiter=';')

        next(csvreader)

        for row in csvreader:
            if not row:
                continue

            mycourse = course.Course(row[1], row[5], row[2], row[4], int(row[6]))

            students.append(student.Student(row[0], row[3], dataSheet.DataSheet(mycourse), row[7]))

        return students

    # for student in studentlist:
    #     join = 0
    #     if not joinedlist:
    #         joinedlist.append(student)
    #         continue
    #
    #     for joined in joinedlist:
    #         if joined.image_url == student.image_url:
    #             join = 0
    #             student.datasheet.add_course(joined.datasheet.courses)
    #             continue
    #         else:
    #             join = 1
    #
    #     if join == 1:
    #         joinedlist.append(student)
