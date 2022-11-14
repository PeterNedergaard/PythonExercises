import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import auc, roc_curve, confusion_matrix

# 2
data = pd.read_csv("AB_NYC_2019.csv")

# 3
data['is_cheap'] = data['price'] < data['price'].median()

# 4
neigh = KNeighborsClassifier(n_neighbors=7)

# 5
X = data[['longitude', 'latitude']]

# 6
X_train, X_test, y_train, y_test = train_test_split(X, data['is_cheap'], test_size=0.33, random_state=42)

# 7
neigh.fit(X_train, y_train)

# 8
y_pred = neigh.predict(X_test)

# 9
fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=True)
auc = auc(fpr, tpr)

# 10
print(data['neighbourhood'])
data['neighbourhood'] = pd.get_dummies(data['neighbourhood'])
print(data['neighbourhood'])
