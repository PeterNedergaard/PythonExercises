import numpy as np

a = np.arange(0, 27).reshape((3, 3, 3))

first = a[1, 1, :]
second = a[:, 1, 0]
third = a[0, :, -1]

print(a)
print()
print(first)
print()
print(second)
print()
print(third)
