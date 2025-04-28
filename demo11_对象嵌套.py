# 案例1:将学生的信息和班级的信息联系起来
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         message = f"我叫{self.name},今年{self.age}岁了"
#         print(message)
#
# s1 = Student("张三", 19)
# s1.info()
# s2 = Student("李四", 20)
# s2.info()
# s3 = Student("王五", 19)
# s3.info()
#
# class Classes:
#     def __init__(self,title):
#         self.title = title
#         self.students_list = []
#
#     def add(self,student):
#         self.students_list.append(student)
#
#
# c1 = Classes("高一59班")
# c1.add(s1)
# c1.add(s2)
# c2 = Classes("高一60班")
# c2.add(s3)
#
# print(c1.title)
# for student in c1.students_list:
#     print(student.name)
#
# print(c2.title)
# for student in c2.students_list:
#     print(student.name)

# 案例2:将小赵的上级全部找出来
class UserInfo:
    def __init__(self,name,prev):
        self.name = name
        self.prev = prev
yj = UserInfo("亚军",None)
wpq = UserInfo("武沛齐",yj)
gz = UserInfo("光照",wpq)
xz = UserInfo("小赵",gz)

print(xz.name)
print(xz.prev.name)
print(xz.prev.prev.name)
print(xz.prev.prev.prev.name)