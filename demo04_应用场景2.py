# 实现一个用户注册功能

# 以前的版本
# user_list = []
#
# while True:
#     user = input("用户名: ")
#     if user.upper() == "Q":
#         break
#     pwd = input("密码: ")
#
#     group = {"name":user, "password":pwd}
#     user_list.append(group)
# # 查看所有的用户名和密码
#
# for ele in user_list:
#     print(ele["name"])
#     print(ele["password"])

# 面向对象版本
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
    
    group = UserInfo(user, pwd)
    user_list.append(group)

for ele in user_list:
    print(ele.username, ele.password)
