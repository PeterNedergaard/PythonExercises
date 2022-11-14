import numpy as np


def any_combination(aar,bydel,alder,statkode):

    data = np.genfromtxt("befkbhalderstatkode.csv", delimiter=',', dtype=np.uint, skip_header=1)

    mask = ((data[:, 0] == aar) & (data[:, 1] == bydel) & (data[:, 2] == alder) & (data[:, 3] == statkode))

    a = data[mask]

    print(a[:, 4].sum())


any_combination(statkode=5180, bydel=1, alder=0, aar=2015)
