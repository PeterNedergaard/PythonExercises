import matplotlib.pyplot as plt

categories = ["10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "90-100%"]
values = []


def make_chart(list_of_students):

    for i in range(1, 10):
        curr_range = i * 10
        numb_in_category = 0

        for student in list_of_students:
            if curr_range <= student.get_study_prog() <= curr_range + 9:
                numb_in_category += 1

        values.append(numb_in_category)

    print(values)

    fig = plt.figure(figsize=(10, 5))

    plt.bar(categories, values, color='maroon', width=0.4)

    plt.xlabel("Category")
    plt.ylabel("Numb. of students")
    plt.title("Student study progression")
    plt.show()
