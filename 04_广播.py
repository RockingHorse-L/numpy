import numpy as np
# shape (4, 3)
a = np.array([
        [0, 0, 0],
        [10, 10, 10],
        [20, 20, 20],
        [30, 30, 30]
])
# shape(1, 3)
b = np.array([0, 1, 2])
#shape (4, 1)
c = np.array([[1], [2], [3], [4]])
print(a + b)
print(a + c)