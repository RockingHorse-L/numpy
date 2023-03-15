import numpy as np

box = np.array(
        [2, 2, 20, 15]
)
boxes = np.array(
        [
            [15, 12, 25, 21],
            [12, 10, 4, 20]
        ]
)
# print(f'box的面积{abs((box[2] - box[0]) * (box[3] - box[1]))}')
#
# print(f'box的面积{abs((boxes[0, 2] - boxes[0, 0]) * (boxes[0, 3] - boxes[0, 1]))}')
#
# print(f"相交的面积为：{abs((box[2]-boxes[0, 0])*(box[3]-boxes[0, 1]))}")
print(boxes[:, 2])