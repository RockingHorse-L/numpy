import numpy as np

item = np.array([
            [3,5,8],
            [4,6,5],
            [3,8,3],
            [2,6,9]
])

person = ("球球","冷檬","蘑菇头")

scores = np.sum(item, axis=1)
num = 0
for data in scores:
    num += 1
    if data == max(scores):
        print(f"第{num}个同学最喜欢跳舞")
score = np.sum(item, axis=0)
for location,i in enumerate(score):
    if i == max(score):
        print(f"{person[location]}受欢迎")
# score = item.sum(axis=0)
# av = item.var(axis=0)
# print(score)
# print(av)
#
# print(f'{av.min()}')