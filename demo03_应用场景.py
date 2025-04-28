# 场景一 将相同的参数传递给不同的应用
# 函数版
# def send_email(to,title,content,img):
#     pass
#
#
# def send_dingding(to,title,content,img):
#     pass
#
#
# def send_weixin(to,title,content,img):
#     pass
#
#
# send_email("glz@163.com","发奖金了","每人100w","xxx.png")
# send_dingding("glz@163.com","发奖金了","每人100w","xxx.png")
# send_weixin("glz@163.com","发奖金了","每人100w","xxx.png")

# 面向对象版

# class Message:
#
#     def send_email(self):
#         print(self.to,self.title,self.content,self.img)
#     def send_dingding(self):
#         print(self.to,self.title,self.content,self.img)
#     def send_weixin(self):
#         print(self.to,self.title,self.content,self.img)
#
#
# obj = Message()
# obj.to = "glz@163.com"
# obj.title = "发奖金了"
# obj.content = "每人100w"
# obj.img = "xxx.png"
#
# obj.send_email()    # 通过对象调用send_email方法时,对象会当作参数传给self,也就是说self里有to,title,content,img
# obj.send_dingding()
# obj.send_weixin()

# 面向对象优化版

class Message:
    def __init__(self,to,title,content,img):
        self.to = to
        self.title = title
        self.content = content
        self.img = img

    def send_email(self):
        print(self.to, self.title, self.content, self.img)
    def send_dingding(self):
        print(self.to, self.title, self.content, self.img)
    def send_weixin(self):
        print(self.to, self.title, self.content, self.img)


obj = Message("glz@163.com", "发奖金", "每人100w", "xxx.png")    #第一步创建一个空对象,第二步执行init方法
# 往空对象里写一个to,to的值等于传递进来的"glz@163.com",同理,title,content,img也一样

obj.send_email()
obj.send_dingding()
obj.send_weixin()