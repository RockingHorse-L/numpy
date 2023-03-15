import numpy as np

a = np.array([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
])
# amin()&amax() 用于计算数组中的元素沿指定轴的最小&大值
# (3, 3)
print(a.shape)
print(np.amin(a))
print(np.amin(a, axis=0))