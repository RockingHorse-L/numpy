import numpy as np
# a1 = np.array([1, 2, 3, 4])
# print(a1)
# print(a1[0])
# print(a1[2])
# a2 = np.array([
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ])
# print(a2[2])
# print(a2[2, 1])
# print(a2[:, 2])
a3 = np.array([
[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
[[20, 21, 22], [23, 24, 25], [26, 27, 28]],
[[30, 31, 32], [33, 34, 35], [36, 37, 38]]
])
# print(a3.shape)
# print(a3[2])
# print(a3[2, 0])
# print(a3[2, 0, 1])
# print(a3[:, 1, 2])
# print(a3[1, 2])
print(a3[0, :])
print(a3[0, :, 1])
print(a3[:, 1])
print(a3[:, 1, 0])