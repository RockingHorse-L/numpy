"""
    ndarry的形状

"""
import numpy as np

a = np.array([
                [1, 2, 3],
                [4, 5, 6]
])

#维度：2
print(a.ndim)
# (2, 3) 矩阵的长度
print(a.shape)
#元素个数
print(a.size)
#类型
print(a.dtype)
#字节大小
print(a.itemsize)