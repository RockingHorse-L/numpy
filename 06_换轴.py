import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
print(a.shape)

#转置
print(a.T)
b = a.swapaxes(1, 0)
print(b.shape)
print(b)