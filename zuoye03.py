import numpy as np

datas = np.ones(shape=[5, 5], dtype="i4")
"""
[
[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 ]
"""
print(datas)
datas[1:4, 1:4] = 0
print(datas)