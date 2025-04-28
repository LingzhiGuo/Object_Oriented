class Police:
    def __init__(self,name):
        self.name = name
        self.score = 100

    def help(self):
        self.score = self.score + 50


zs = Police("张三")
ls = Police("李四")


print(zs.score)
zs.help()
print(zs.score)