import numpy as np


def any_combination(aar, bydel=None, statkode=None, alder=None):

    data = np.genfromtxt("befkbhalderstatkode.csv", delimiter=',', dtype=np.uint, skip_header=1)

    if alder is None:
        mask = ((data[:, 0] == aar) & (data[:, 1] == bydel) & (data[:, 3] == statkode))
    else:
        mask = ((data[:, 0] == aar) & (data[:, 1] == bydel) & (data[:, 2] == alder) & (data[:, 3] == statkode))

    # aar_mask = data[:, 0] == aar
    #
    # alder_mask = data[:, 2] == alder
    #
    # mask = (aar_mask & (data[:, 1] == bydel) & alder_mask & (data[:, 3] == statkode))

    a = data[mask]

    return a


print(any_combination(statkode=5100, bydel=3, aar=1992, alder=3)[:, 4].sum())
