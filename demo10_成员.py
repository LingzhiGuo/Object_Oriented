class Message:
    country = "中国"             # 类变量, 属于类, 调用的时候既可以用Message.country,也可以用obj1.country
    def __init__(self, n, m):   # 绑定方法,对象.方法名调用且调用时自动传递self
        self.x1 = n             # obj1.x1 = 上海 和 obj1.x2 = 北京 是实例变量,属于对象
        self.x2 = m

    def send(self, to, content):    # # 绑定方法,对象.方法名调用且调用时自动传递self
        print(self.x1, self.x2, to, content)

obj1 = Message("上海", "北京")
obj1.send("xx","xxx")

# 1. 变量
# 1.1 实例变量, 属于对象
# 1.2 类变量,属于类.(每个对象中都有同样的值,为了避免内存开销,使用类变量保存一份即可)


# 2. 方法

# 2.1 绑定方法
# 定义时: 至少有一个self参数,哪个对象调用此方法时i,self就是谁
# 调用时: 对象.方法名称()
#
#
# 2.2 静态方法:当方法中不会用到任何对象中封装的值时,可以使用静态方法
# 定义时: 可以有任意个参数,python内部不会帮他传递任何参数, 并且前一行要加上: @staticmethod
# 调用时: 可以是: 类名.方法名称(...)
#       也可以是: 对象.方法名称(...) --python独有
#
# 2.3 类方法: 在方法中不需要用对象,而是需要使用当前类时,就需要用类方法,该种情况使用较少
# 定义时: 至少有一个cls参数,cls是python内部自动传递的,cls的值等于当前类名
# 调用时: 可以是: 类名.方法名称(...)   cls = 当前类
#       也可以是: 对象.方法名称(...)  cls = 当前类

# class Message:
#     def __init__(self,n,m):
#         self.x1 = n
#         self.x2 = m
#
#     def send(self,to,content):
#         print(self.x1,self.x2,to,content)
#
#     @staticmethod
#     def show():
#         print("xxxx")
#
#     @classmethod
#     def get_info(cls,age):
#         print(cls,"hahahaha",age)

## 绑定方法调用
# object = Message("上海","北京")
# object.send("房山","浦东")  # 上海 北京 房山 浦东

## 静态方法调用
# Message.show()
# object.show()   # 只有python编程语言可以这么操作

## 类方法调用
# Message.get_info(18)
# object.get_info(18) # # 只有python编程语言可以这么操作

print("_"*30)

# 3. 属性
# 示例1
# class Message:
#     def __init__(self,n,m):
#         self.x1 = n
#         self.x2 = m
#     @property
#     def send(self):
#         return "123"
#
# object = Message("x","y")
# data = object.send              # 这里不需要加括号
# print(data)

# 示例2
# 分页功能
# class Pagination:
#     def __init__(self,page,per_page_count=10):
#         self.page=int(page)
#         self.per_page_count=per_page_count
#     @property
#     def start(self):
#         return (self.page-1)*self.per_page_count
#     @property
#     def end(self):
#         return self.page*self.per_page_count
# def run():
#     data_list = []
#     for i in range(1,501):
#         data_list.append("移动-{}".format(i))
#
#     while True:
#         page = input("请输入页面:")
#
#         pg = Pagination(page)
#
#         page_list = data_list[pg.start:pg.end]
#         for item in page_list:
#             print(item)
#
#
# if __name__ == '__main__':
#     run()

# 关于属性的拓展
# class Message:
#     def __init__(self,n,m):
#         self.x1 = n
#         self.x2 = m
#     @property
#     def send(self):
#         return "123"
#
#     @send.setter
#     def send(self,value):   # 2. 再写一个相同的方法名,被方法名.setter装饰,可以做到设置参数的效果
#         self.x1 = value
#         self.x2 = value*2
#     @send.deleter
#     def send(self):
#         print("删除了")
#
#
# object = Message(11,22)
# print(object.send)  # 1. 通过property装饰了send方法后,可以直接通过对象.方法名,不加括号来调用
# object.send = 999   # 这里可以把999传递给value,从而达到更改self.x1等的效果
# print(object.x1)
# print(object.x2)
# del object.x1


"""语法规则:
以object.send调用的时候,会执行@property下的函数
以object.send = 999调用的时候,会执行@send.setter下的函数
以del object.x1调用的时候,会执行@send.deleter下的函数"""

# 另一种写法:

class Message:
    def __init__(self,n,m):
        self.x1 = n
        self.x2 = m

    def getx(self):
        pass

    def setx(self,value):
        pass

    def delx(self):
        pass

    x = property(getx,setx,delx)

object = Message(10,20)

object.x        # 调用getx方法并获取返回值
object.x = 123  # 调用setx方法
del object.x    # 调用delx
