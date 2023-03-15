"""
    深拷贝:会拷贝内存里面的东西
    浅拷贝:内存的东西不会拷贝，只会拷贝外面的list就是内存的
"""
import copy

# #浅拷贝
# users = ['tt', 'shurui',['球球']]
# usersCopy = copy.copy(users)
# # 情况1：
# # users[0] = '腿腿'
# # print(users)
# # print(usersCopy)
#
# # 情况2：
# users[2].append('柠檬')
# print(users)
# print(usersCopy)

# 深拷贝
users = ['tt', 'shurui',['球球']]
users_copy = copy.deepcopy(users)
# users[0] = '腿腿'
users.append('柠檬')
print(users)
print(users_copy)
