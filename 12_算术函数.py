import numpy as np

a = np.arange(1, 10, dtype=np.int8).reshape(3, 3)
b = np.array([2, 2, 1])
print(a)
print(b)
print('*'*20)
# 减
# print(np.subtract(a, b))
# # 乘
# print(np.multiply(a, b))
# # 数组对应位置元素做除法
# print(np.divide(a, b))
# 只保留整数结果
# print(np.floor_divide(a ,b))
# 计算两数组对应位置元素的余数
print(np.mod(a, b))
# 计算 a 的 b 次方
print(np.power(a, b))
# e的 1次方
print(np.exp(1))
