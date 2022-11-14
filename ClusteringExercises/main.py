import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
from itertools import cycle

data_raw = pd.read_csv("iris_data.csv", decimal=',')

data_species = data_raw['Species']
data_2d = data_raw.drop(columns=['Petal length', 'Petal width', 'Species'])
data_2d_np = data_2d.to_numpy()


def mean_shift(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.2,
                                   n_samples=n_samples)
    ms = MeanShift(bandwidth=bandwidth)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters: ' + str(n_clusters))

    return labels, cluster_centers, n_clusters


labels, cluster_centers, n_clusters = mean_shift(data_2d_np)
print(labels)
print(cluster_centers)
print(n_clusters)

fig = plt.figure()
ax = fig.add_subplot(111)

colors = cycle('bgrcmy')
# print(list(zip(range(3), colors)))

for k, col in zip(range(n_clusters), colors):
    my_members = (labels == k)
    cluster_center = cluster_centers[k]

    x, y = data_2d_np[my_members, 0], data_2d_np[my_members, 1]
    ax.scatter(x, y, c=col, linewidth=0.2)
    ax.scatter(cluster_center[0], cluster_center[1], c='k', s=50, linewidth=0.2)

plt.show()
