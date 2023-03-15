import numpy as np
nums = [
[1, 2, 3],
[4, 5, 6]
]
"""
 相同点: array和asarray将结构数据转换成ndarray数组
 区别:
 np.array会开辟一块内存，对于大数组来说，会存在大量赋值操作，速度慢且不节约内存
 np.asarray 相当于新增加一个指向当前内存引用，其中一个引用数据被修改，其他引用数据也会被修
改
"""
a = np.array(nums)
a1 = np.array(a)
a2 = np.asarray(a)
a[0, 0] = 100
# 1479978336880
print(a)
# 1480656731568
print(a1)
# 1479978336880
print(a2)
print(id(a), id(a1), id(a2))