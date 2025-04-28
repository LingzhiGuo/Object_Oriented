# 父类, 基类
# class Foo:
#     pass

# 子类, 派生类
# class Bar(Foo):
#     pass

print("-"*30)

# class Base:
#     def f1(self):
#         print("Base.f1")
#
# class Son(Base):
#     def f2(self):
#         print("Son.f2")
#
#
# obj = Son()
# obj.f2()
# obj.f1()    # 先去子类里找方法,子类里找不到再去父类里找

# 注意: self到底是谁?
# 无论方法是从子类还是父类中找到的,哪个对象调用的这个方法,self就是这个对象
print("-"*30)
# 易错点1

# class Base:
#     def f1(self):
#         print(self.age)
#
# class Son(Base):
#     def f2(self):
#         print(self.name)
#
# obj = Son()
# obj.name = "移动"
# obj.age = 100
#
# obj.f2()    # 移动
# obj.f1()    # 100

print("-"*30)
# 易错点2
# class Base:
#     def f1(self):
#         print("base.f1")
#
# class Son(Base):
#     def f1(self):
#         print("son.f1")
#     def f2(self):
#         print("son.f2")
#
# obj = Son()
# obj.f2()    # son.f2
# obj.f1()    # son.f1
print("-"*30)
# 易错点3
# class Base:
#     def f1(self):
#         print("base.f1")
#
# class Son(Base):
#     def f1(self):
#         print("son.f1")
#     def f2(self):
#         print("son.f2")
#         self.f1()
#
#
# obj = Son()
# obj.f2()    # son.f2 son.f1

print("-"*30)
# 易错点4
# class Base:
#     def f1(self):
#         print("base.f1")
#     def f2(self):
#         print("base.f2")
#         self.f1()
# class Son(Base):
#     def f1(self):
#         print("son.f1")
#
#
# obj = Son()
# obj.f2()    # base.f2 son.f1

print("-"*30)
# 易错点5
# class Base:
#     def f1(self):
#         print("base.f1")
#     def f2(self):
#         print("base.f2")
#         self.f1()
# class Son(Base):
#     def f1(self):
#         print("son.f1")
#
#
# obj = Base()
# obj.f2()    # base.f2 base.f1


# 多继承: 一个类可以继承多个类(其他语言只能继承一个类)

class Base:
    def f1(self):
        print("base.f1")

class Foo:
    def f2(self):
        print("foo.f2")

class Bar(Base, Foo):   # 找方法时优先从左边的Base找,找不到再去Foo中找
    pass

obj = Bar()
obj.f1()
obj.f2()
