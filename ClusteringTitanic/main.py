import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import MeanShift, estimate_bandwidth

data = pd.read_csv("titanic_train.csv")

# Drop columns
data = data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

# Change sex to 1 or 0
le = preprocessing.LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])

# One-hot-encode the Embarked column
data[['C', 'Q', 'S']] = pd.get_dummies(data['Embarked'])
data = data.drop(columns='Embarked')

# Drop rows with missing values
data = data.dropna()

# Best bandwidth to use
bandwidth = estimate_bandwidth(data)
# print(bandwidth)

# Fit data to a meanshift model
ms = MeanShift(bandwidth=bandwidth)
ms.fit(data)

# How many clusters do we get
labels = ms.labels_
labels_unique = np.unique(labels)
cluster_centers = ms.cluster_centers_
n_clusters = len(labels_unique)
# print(n_clusters)

# Add cluster label to each row
data['ClusterLabel'] = labels

# Get mean values of each cluster group
data_cluster = data.groupby(['ClusterLabel']).mean()
data_cluster['Count'] = data.groupby(['ClusterLabel']).size()

print(data_cluster)
