import numpy as np

import exercise1
import exercise2

data = np.genfromtxt("befkbhalderstatkode.csv", delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}

peopledata = np.loadtxt("demographic_cleaned.csv", dtype=np.uint, delimiter=',')
citydata = np.loadtxt("DKstat_bykoder.csv", dtype=str, delimiter=';')

# print(exercise1.amount_in_each_area(data, neighb))

# exercise1.plot_from_dict(exercise1.amount_in_each_area(data, neighb))

# print(exercise1.above_age_in_year(data, 2015, 65)[:, 4].sum())

# print(exercise1.amount_not_in_dk(exercise1.above_age_in_year(data, 2015, 65))[:, 4].sum())

# exercise1.plot_changes_in_people(data)

# print(exercise2.highest_perc_male(peopledata, citydata, 2008))

# print(exercise2.five_largest_citites(peopledata))

# exercise2.five_cities_plot(peopledata)


