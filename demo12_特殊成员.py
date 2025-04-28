# 1. __init__,类()--> 初始化方法
# class Foo:
#     def __init__(self,name):
#         self.name = name
#
# object = Foo("root")


# 2.__new__,构造方法,创建空对象

# class Foo(object):
#     def __init__(self,name):
#         print(2)
#         self.name = name
#
#     def __new__(cls,*args,**kwargs):
#         print(1)
#         empty_obj = object.__new__(cls)
#         return empty_obj
#
# # 1. 调用__new__去创建空对象
# # 2. 调用__init__给对象初始化
# object = Foo("武沛齐")

# 3. __call__, 对象()可以调用
# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         return 666
# # 类() --> init
# object = Foo("武沛齐")
# # 对象() --> call
# data =object()
# print(data)

# 4. __str__
# class Foo(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# object = Foo("武沛齐",22)  # <__main__.Foo object at 0x0000029625D91490>
# print(object)
print("-"*30)
# class Foo(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name}--{self.age}"
# # 查看对象信息
# object = Foo("武沛齐",22)
# print(object)
#
# # 将对象转换成str
# data = str(object)
# print(data)

# 5. __dict__,以字典的形式查看对象的所有成员
# class Foo(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# object = Foo("武沛齐",22)
# print(object.__dict__)

# 6. __getitem__, __setitem__,__delitem__

# class Foo(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         return 999
#
#     def __setitem__(self, key, value):
#         pass
#
#     def __delitem__(self, item):
#         pass
#
# object = Foo("武沛齐",22)
# data = object["xxxx"]   # 对象["xxx"]会执行__getitem__
# print(data)
#
# object["xxxx"] = 123    # 对象["xxx"] = abc会执行__setitem__,xxx传入key,abc传入value
# del object["xxxx"]      # del 对象["xxx"]会执行__delitem__

# 7. __add__:让对象和对象相加
class Foo(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __add__(self,other):
        return self.age+other.age

object1 = Foo("武沛齐",22)
object2 = Foo("光照",12)

v = object1 + object2
print(v)


