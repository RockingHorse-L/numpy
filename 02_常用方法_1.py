import numpy as np

print(np.array([1, 2, 3], dtype = "f4"))
print(np.array([1.2, 2.2, 3]))
#要求维度
print(np.array([1, 2, 3, 4, 5], ndmin = 2))
print(np.array([1, 2, 3], dtype=str))
print(np.array([range(i, i + 5) for i in [1, 2, 3]]))
#生成5行5列
print(np.zeros(shape=[5, 5], dtype="i4"))
print(np.ones(shape=[5, 5], dtype="i4"))
print(np.array(["1.1", "2.2", "3.3"], dtype="S").astype("f4"))

#所有非零元素的索引
nums = np.nonzero(np.array([1, 0, 2, 3, 0, 4]))
print(nums)

print(np.full(shape=[5, 5], fill_value=1.5, dtype=np.float_))

print(np.eye(10))
#数组元素为随机值
print(np.empty(shape=(5, 5)))
#返回num个等间距的样本
print(np.linspace(1, 10 ,5))
# 生成5行5列
print(np.random.random((5, 5)))
#生成[0, 10)且3行3列的随机数
#生成的数据包括起始值和结束值，单不包括结束值本身
#(3, 3)生成3行3列
print(np.random.randint(0, 10, (3, 3)))
print(np.random.normal(0, 1, (3, 3)))
print(np.array([1, 2, 3]).itemsize)