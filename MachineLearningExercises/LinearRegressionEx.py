import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale

x = load_diabetes().data
y = load_diabetes().target

x_reshape = np.array(x).reshape(-1, 1)

model = LinearRegression()
model.fit(x_reshape, y)
