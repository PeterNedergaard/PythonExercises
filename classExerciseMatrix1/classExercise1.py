
import numpy as np

a = np.arange(10, 30).reshape(4, 5)


yellow = a[0, 0]
cyan = a[:, 1::2]
red = a[0, 1:4]
green = a[:3, 2]
blue = a[::2, -1]

print(a)
# print()
# print(yellow)
print()
print(cyan)
# print()
# print(red)
# print()
# print(green)
# print()
# print(blue)
