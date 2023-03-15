"""
    2. 给定三个点，求夹角
    cosA=[b²＋c²－a²]/(2bc)
    cosB=[a²＋c²－b²]/(2ac)
    cosC=[a²＋b²－c²]/(2ab)
"""
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
points = []
point1 = Point(2, 3)
point2 = Point(4, 4)
point3 = Point(5, 2)
points.append(point1)
points.append(point2)
points.append(point3)
a = math.sqrt((point2.x - point3.x) * (point2.x - point3.x) + (point2.y - point3.y) * (point2.y - point3.y))
b = math.sqrt((point1.x - point3.x) * (point1.x - point3.x) + (point1.y - point3.y) * (point1.y - point3.y))
c = math.sqrt((point1.x - point2.x) * (point1.x - point2.x) + (point1.y - point2.y) * (point1.y - point2.y))
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))

print(f"角度A为：{A}")
print(f"角度B为：{B}")
print(f"角度C为：{C}")