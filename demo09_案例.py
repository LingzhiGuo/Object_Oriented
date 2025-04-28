# 反射
# data = getattr(对象,"成员名称")   # 等价于:对象.成员名称
# print(data)
#
# setattr(对象,"成员名称",值)        # 等价于:对象.成员名称 = 值
# 好处:直接以字符串的形式操控
print("-"*30)

# 例1
# class Foo:
#     pass
#
# obj = Foo()
# obj.x1 = "北京"
# obj.x2 = "上海"
# setattr(obj,"x3","南京")  # obj.x3 = "南京"
#
# data = getattr(obj,"x1")    # 相当于obj.x1
# data2 = getattr(obj,"x3")
# print(data,data2)
print("-"*30)
# 例2

# if判断版本
# class Foo:
#     def __init__(self):
#         self.x1 = "北京"
#         self.x2 = "上海"
#
# obj = Foo()
# choice = input("请选择:")  # x1/x2
#
# if choice == "x1":
#     print(obj.x1)
# elif choice == "x2":
#     print(obj.x2)

print("-"*30)
# 面向对象版本
# class Foo:
#     def __init__(self):
#         self.x1 = "北京"
#         self.x2 = "上海"
#
# obj = Foo()
# choice = input("请选择:")  # x1/x2
#
# data = getattr(obj,choice)
# print(data)
print("-"*30)
# 如何获取对象中封装的所有的值
# class Foo:
#     def __init__(self):
#         self.x1 = "北京"
#         self.x2 = "上海"
#
# obj = Foo()
# obj.x3 = "南京"
#
# print(obj.__dict__)

print("-"*30)

# 例3:请加载配置文件settings.ini中的所有数据
# 函数版方法
import configparser


# def run():
#     # 1. 请去加载配置文件
#     config_dict = {}
#
#     parser = configparser.ConfigParser()
#     parser.read("settings.ini",encoding="utf-8")
#     options = parser.items("settings")
#     for k,v in options:
#         config_dict[k] = v
#
#     print(config_dict)
#     # 2. 后续使用这个配置
#     print(config_dict['window_x'])
#     print(config_dict['window_y'])
#     print(config_dict['windowed_width'])
#     print(config_dict['windowed_height'])
#     print(config_dict['fullscreen_width'])
#     print(config_dict['fullscreen_height'])
#
#
# if __name__ == "__main__":
#     run()
print("-"*30)
# 面向对象基础版本,打印出来的全是字符串类型,如果需要比较值的大小有所不便
# class Settings:
#     def __init__(self):
#         self.proxy_host = None    # 这里先给对象加一个window_x方法,目的是在后续使用这个配置的时候只要输入对象.就会自动弹出方法
#         self.proxy_port = None
#         self.proxy_id = None
#         self.proxy_secret = None
#         self.min_inventory = None
#
#
# def run():
#     # 1. 请去加载配置文件
#     settings_obj = Settings()
#
#     parser = configparser.ConfigParser()
#     parser.read("settings.ini",encoding="utf-8")
#     options = parser.items("settings")
#     for k,v in options:
#         setattr(settings_obj,k,v)   # 等价于settings_obj.k = v
#
#     # 2. 后续使用这个配置
#     print(settings_obj.proxy_host,type(settings_obj.proxy_host))        # tunnel2.net <class 'str'>
#     print(settings_obj.proxy_port,type(settings_obj.proxy_port))        # 17955 <class 'str'>
#     print(settings_obj.proxy_id,type(settings_obj.proxy_id))            # E007BD5F <class 'str'>
#     print(settings_obj.proxy_secret,type(settings_obj.proxy_secret))    # ZDX3457XRTG <class 'str'>
#     print(settings_obj.min_inventory,type(settings_obj.min_inventory))  # 50 <class 'str'>
#
#
# if __name__ == "__main__":
#     run()
print("-"*30)
# 面向对象改进版

class Settings:
    def __init__(self):
        self.proxy_host = str    # 这里先给对象加一个window_x方法,目的是在后续使用这个配置的时候只要输入对象.就会自动弹出方法
        self.proxy_port = int
        self.proxy_id = str
        self.proxy_secret = str
        self.min_inventory = int


def run():
    # 1. 请去加载配置文件
    settings_obj = Settings()

    parser = configparser.ConfigParser()
    parser.read("settings.ini",encoding="utf-8")

    for filed,data_type in settings_obj.__dict__.items():
        # print(filed,data_type)
        # 1.1 根据字段 proxy_host去ini文件中获取对应值
        data_string = parser.get("settings",filed)      # 获取到settings部分中filed键对应的值
        # print(data_string,type(data_type))
        real_data = data_type(data_string)                     # 根据__init__中提前定义的类型进行转换
        # print(real_data,type(real_data))
        setattr(settings_obj,filed,real_data)                  # 转换完数据类型后写入方法

    # 2. 后续使用这个配置
    print(settings_obj.proxy_host,type(settings_obj.proxy_host))        # tunnel2.net <class 'str'>
    print(settings_obj.proxy_port,type(settings_obj.proxy_port))        # 17955 <class 'int'>
    print(settings_obj.proxy_id,type(settings_obj.proxy_id))            # E007BD5F <class 'str'>
    print(settings_obj.proxy_secret,type(settings_obj.proxy_secret))    # ZDX3457XRTG <class 'str'>
    print(settings_obj.min_inventory,type(settings_obj.min_inventory))  # 50 <class 'int'>


if __name__ == "__main__":
    run()


