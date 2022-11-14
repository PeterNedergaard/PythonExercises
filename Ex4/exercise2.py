import matplotlib.pyplot as plt
import numpy as np


def highest_perc_male(peopledata, citydata, year):
    percentdict = {}

    for city in citydata:
        malepercent = male_percent_by_city(peopledata, int(str(city[0]).strip()), year)

        if malepercent == 0:
            continue

        percentdict[city[1]] = malepercent

    percentdict = dict(sorted(percentdict.items(), key=lambda x: x[1]))

    highestcity = list(percentdict)[-1]
    highestpercent = percentdict.get(highestcity)

    return highestcity + " with " + str(highestpercent) + "% male"


def male_percent_by_city(peopledata, citycode, year):
    citydatamask = ((peopledata[:, 0] == citycode) & (peopledata[:, 3] == year))

    citydata = peopledata[citydatamask]

    malepercent = 0

    if citydata[:, 4].sum() > 0:
        mendata = citydata[citydata[:, 1] == 1]

        malepercent = (mendata[:, 4].sum() / citydata[:, 4].sum()) * 100

    return round(malepercent, 2)


def city_name_by_code(citycode):
    citydata = np.loadtxt("DKstat_bykoder.csv", dtype=str, delimiter=';')

    for data in citydata:
        if int(str(data[0]).strip()) == citycode:
            return str(data[1]).strip()


def five_cities_plot(peopledata):
    citycodelist = [84, 147, 400, 85, 751]

    for citycode in citycodelist:
        citydict = {}

        for year in range(2008, 2021):
            mask = ((peopledata[:, 0] == citycode) & (peopledata[:, 3] == year))

            data = peopledata[mask]

            citydict[year] = data[:, 4].sum()

        x, y = zip(*citydict.items())
        plt.plot(x, y, label=city_name_by_code(citycode))

    plt.title("Increase in population, 2008-2020")
    plt.xlabel("Year")
    plt.ylabel("Population in million")
    plt.legend(loc='upper left')
    plt.show()
