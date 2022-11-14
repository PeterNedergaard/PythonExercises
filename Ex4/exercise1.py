import matplotlib.pyplot as plt


def amount_in_each_area(data, neighb):
    mydict = {}

    for i in neighb:
        mask = ((data[:, 0] == 2015) & (data[:, 1] == i))

        dd = data[mask]

        mydict[neighb[i]] = dd[:, 4].sum()

    return dict(sorted(mydict.items(), key=lambda x: x[1]))


def plot_from_dict(mydict):
    plt.figure(figsize=(10, 7))
    plt.xticks(rotation=30)
    plt.bar(mydict.keys(), mydict.values(), width=0.5)
    plt.show()


def above_age_in_year(data, year, age):
    mask = ((data[:, 0] == year) & (data[:, 2] >= age))

    dd = data[mask]

    return dd


def amount_not_in_dk(data):
    mask = ((data[:, 3] == 5120) | (data[:, 3] == 5110) | (data[:, 3] == 5104))

    dd = data[mask]

    return dd


def plot_changes_in_people(data):
    mydict = {}

    for i in range(1992, 2016):
        mask = ((data[:, 0] == i) & (data[:, 1] == 2) | (data[:, 1] == 4))

        dd = data[mask]

        mydict[i] = dd[:, 4].sum()

    x, y = zip(*mydict.items())
    plt.plot(x, y)
    plt.show()
