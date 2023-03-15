"""
    自定义User类添加到列表UserList中，使用代码进行演示copy()和deepcopy() 区别
"""
import copy


class User:
    def __init__(self, name):
        self.name = name

UserList = [['hhh']]

UserList.append(User('tt').name)
UserList.append(User('shurui').name)
print(UserList[1])

# 浅拷贝
usersList = copy.copy(UserList)
UserList.append(User('hh').name)
print(UserList)
print(usersList)


#深拷贝
# usersList = copy.deepcopy(UserList)
# UserList.append(User('hh').name)
# print(UserList)
# print(usersList)