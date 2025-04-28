# 例1
# class Message:
#     def send(self,to,content):
#
#         print(self.x1,self.x2,to,content)
#
#
# obj = Message()
#
# obj.x1 = "上海"
# obj.x2 = "北京"
#
# obj.send("glz@0127.com","hello")

# 例2
# class Message:
#
#     def send(self, to, content):
#         print(self.x1, self.x2, to, content)
#
#
# obj1 = Message()
#
# obj1.x1 = "上海"
# obj1.x2 = "北京"
#
# obj2 = Message()
#
# obj2.x1 = "南京"
# obj2.x2 = "山西"
#
# obj1.send("glz@0127.com", "hello")
# obj2.send("glz@0127.com", "hi")

# 例3 特殊的初始化方法
class Message:

    def __init__(self, n, m):
        self.x1 = n
        self.x2 = m

    def send(self, to, content):
        print(self.x1, self.x2, to, content)

# 根据类创建对象时
# 1. 根据类在内存创建对象(空)
# 2. 立即执行类中的__init__方法，为对象初始化属性 空对象, 上海, 北京
obj1 = Message("上海", "北京")
obj1.send("glz@0127.com", "hello")

obj2 = Message("南京", "太原")
obj2.send("glz@0127.com", "hi")

# 小结:
# 1. 对象是根据类创建出来的一块区域,这块区域可以存储值,对象可以找到类中的方法并执行
# 2. __init__是类中的一个特殊方法,此方法在类名()自动执行,一般用于给对象中进行值的初始化
# 3. self本质上就是一个参数,不需要人为传递,python内部会传递,传递的是对象