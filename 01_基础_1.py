"""
    ndarray与python原生list运算效率对比
"""
import random
import time
import numpy as np

a = []
for i in range(10000000):
    a.append(random.random())

t1 = time.time()
total = sum(a)
t2 = time.time()
print(t2 - t1)


#ndarray
b = np.array(a)
t3 = time.time()
total = np.sum(b)
t4 = time.time()
print(t4 - t3)