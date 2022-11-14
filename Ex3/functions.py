import csv


def sort_criteria(e):
    return e['progress']


def get_top_3(list_of_students):
    top3list = []
    studentdict = []
    sortedstudentlist = []

    for student in list_of_students:
        studentdict.append({'student': student, 'progress': student.get_study_prog()})

    studentdict.sort(reverse=True, key=sort_criteria)

    sortedstudentlist = [sub['student'] for sub in studentdict]

    for i in range(0, 3):
        top3list.append(sortedstudentlist[i])

    if len(top3list) < 3:
        raise NotEnoughStudentsException("Not enough students. 3 are required. Your number of students: " +
                                         str(len(top3list)))

    return top3list


class NotEnoughStudentsException(Exception):
    pass


def top_3_to_file(list_of_students):
    top3list = []

    with open("top3output.csv", "w") as f:
        csvwriter = csv.writer(f, delimiter=';')

        try:
            top3list = get_top_3(list_of_students)
        except NotEnoughStudentsException:
            csvwriter.writerow(["Not enough students. 3 students are required"])
        else:
            csvwriter.writerow(["stud_name", "progress in %"])

            for stu in top3list:
                csvwriter.writerow([stu.name, stu.get_study_prog()])
