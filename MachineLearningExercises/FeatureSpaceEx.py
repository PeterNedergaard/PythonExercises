import random
import numpy as np
import matplotlib.pyplot as plt


# 01 Exercise: feature space

# Task: 1/3
def baby_data(amount):
    baby_tuple = []

    for i in range(amount):
        age = random.randint(1, 48)
        height = age*6.5+random.uniform(65, 85)
        weight = age*2+random.uniform(6, 10)

        baby_tuple.append((height, weight, age))

    return np.array(baby_tuple, dtype=int)


# TasK: 2
def plot_3d_feature_space(data_3d):
    x, y, z = data_3d[:, 0], data_3d[:, 1], data_3d[:, 2]

    ax = plt.axes(projection='3d')
    ax.scatter3D(x, y, z)

    ax.set_xlabel("Height")
    ax.set_ylabel("Weight")
    ax.set_zlabel("Age")

    plt.show()


plot_3d_feature_space(baby_data(1000))
