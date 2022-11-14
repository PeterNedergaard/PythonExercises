import numpy as np

data = np.genfromtxt("befkbhalderstatkode.csv", delimiter=',', dtype=np.uint, skip_header=1)

mask = ((data[:, 0] == 2015) & (data[:, 2] == 0) & (data[:, 3] == 5180))

a = data[mask]

print(a[:, 4].sum())

