"""
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 转为一维数组
"""
import numpy as np

arr_3d = np.array([
            [[1, 2],
                [3, 4]],
            [[5, 6],
                [7, 8]]
])
print(arr_3d.shape)
arr_1d = arr_3d.reshape(8, )
print(arr_1d)