import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

data1 = pd.read_csv("task5A.csv", delimiter=",")
df_data1 = pd.DataFrame(data1)

data2 = pd.read_csv("task5B.csv", delimiter=",")
df_data2 = pd.DataFrame(data2)

data3 = pd.read_csv("task5C.csv", delimiter=",")
df_data3 = pd.DataFrame(data3)

data4 = pd.read_csv("task5D.csv", delimiter=",")
df_data4 = pd.DataFrame(data4)


def pct_divorced(year):
    df_year_data = df_data1[df_data1['TID'] == year]
    total_sum = df_year_data[df_year_data['CIVILSTAND'] == "I alt"]['INDHOLD'].sum()
    divorced_sum = df_year_data[df_year_data['CIVILSTAND'] == "Fraskilt"]['INDHOLD'].sum()

    return round((divorced_sum / total_sum) * 100, 2)


def change_in_divorced():
    mydict = {}

    for year in range(2008, 2021):
        mydict[year] = pct_divorced(year)

    return mydict


def pct_never_married():
    df_cities = df_data2['OMRÅDE']
    cities = set(df_cities)

    never_married_dict = {}

    for city in cities:
        df_city_data = df_data2[df_data2['OMRÅDE'] == city]

        total_sum = df_city_data[df_city_data['CIVILSTAND'] == "I alt"]['INDHOLD'].sum()
        never_married_sum = df_city_data[df_city_data['CIVILSTAND'] == "Ugift"]['INDHOLD'].sum()

        never_married_dict[city] = round((never_married_sum / total_sum) * 100, 2)

    return dict(sorted(never_married_dict.items(), key=lambda x: x[1]))


def plot_changes_in_status():
    df_marrital_status = df_data3['CIVILSTAND']
    statuses = set(df_marrital_status)

    change_sum = []

    for status in statuses:
        df_status_data = data3[data3['CIVILSTAND'] == status]
        sum_2008 = df_status_data[df_status_data['TID'] == 2008]['INDHOLD'].sum()
        sum_2020 = df_status_data[df_status_data['TID'] == 2022]['INDHOLD'].sum()

        change_sum.append(round((sum_2020/3) - (sum_2008/3)))

    x_axis = np.arange(len(statuses))

    plt.xticks(x_axis, statuses)
    plt.bar(x_axis, change_sum, 0.5, label='Num. of people')

    plt.xlabel("Marrital status")
    plt.ylabel("Number of people")
    plt.title("Change in marrital statuses from 2008-2022")

    plt.grid()
    plt.legend()
    plt.show()


def plot_married_unmarried():
    df_marrital_status = df_data4['CIVILSTAND']
    statuses = set(df_marrital_status)

    dict_unmarried = {}
    dict_married = {}

    for status in statuses:
        df_status_data = df_data4[df_data4['CIVILSTAND'] == status].iloc[1:, :]

        for age in range(0, 126):
            amount = df_status_data[df_status_data['ALDER'] == str(age) + " år"]['INDHOLD'].item()

            if status == "Ugift":
                dict_unmarried[age] = amount
            if status == "Gift/separeret":
                dict_married[age] = amount

    x1, y1 = zip(*dict_unmarried.items())
    x2, y2 = zip(*dict_married.items())

    plt.plot(x1, y1, label='Unmarried')
    plt.plot(x2, y2, label='Married')

    plt.xlabel("Age")
    plt.ylabel("Amount")
    plt.title("Amount of married and unmarried people in 2020")

    plt.legend()
    plt.show()


# print(change_in_divorced())
# print(pct_never_married())
# plot_changes_in_status()
plot_married_unmarried()
