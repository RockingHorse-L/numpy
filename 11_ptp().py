import numpy as np

# 计算数组中元素最大值与最小值的差（最大值 - 最小值）最小值
a = np.array([
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]
])
print(np.ptp(a))
print(np.ptp(a, axis=0)) # 0轴：X轴每个坐标值的（最大Y - 最小Y）
print(np.ptp(a, axis=1)) # 1轴：Y轴每个坐标值的（最大X - 最小X）