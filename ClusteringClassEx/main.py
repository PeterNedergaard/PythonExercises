import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from itertools import cycle
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation

X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
n_labels = set(y)

fig = plt.figure()
ax = fig.add_subplot(111)

# colors = cycle('bgrcmy')
#
# for k, col in zip(range(len(n_labels)), colors):
#     states = (y == k)
#
#     x, z = X[states, 0], X[states, 1]
#     ax.scatter(x, z, c=col, linewidth=0.2)
#
# plt.show()


model = AffinityPropagation(damping=0.7)
model.fit(X)
p = model.predict(X)
unique_clusters = np.unique(p)

print(p)

colors = list()
for i in range(len(unique_clusters)):
    colors.append(list(np.random.uniform(range(0, 1), size=3)))

for data, i in zip(X, range(len(X))):
    x, z = data[0], data[1]
    col = colors[p[i]]

    ax.scatter(x, z, color=(col[0], col[1], col[2]), linewidth=0.2)


# ax.scatter(X[0:-1], X[1:])
plt.show()
# print(X)
print()
print()
# print(X[:0])
