# 封装
"""
封装,就是将数据封装到一个对象中,后期再去对象中获取已封装的数据
"""


class UserInfo:
    def __init__(self, user, pwd):
        self.username = user
        self.password = pwd


user_list = []

while True:
    user = input("用户名: ")
    if user.upper() == "Q":
        break
    pwd = input("密码: ")

    group = UserInfo(user, pwd) # 将user和pwd封装到对象group中
    user_list.append(group)

for ele in user_list:
    print(ele.username, ele.password)


"""
功能的划分和分装, 将一类方法写到一类里
"""

class ExcelHelper:
    def open(self):
        pass
    def close(self):
        pass

class WordHelper:
    def open(self):
        pass
    def close(self):
        pass