"""
封装
    属于面向对象的三大特征之一 就是隐藏对象的属性和实现细节 仅对外提供公共的访问方式
怎么封装
    函数 类 都是封装的体现
好处
    1. 提高代码的安全性   由 私有化 来保证
    2. 提高代码的复用性   由 函数 来保证
弊端
    代码量增加 因为私有化内容外界想要访问 必须提供公共的访问方式 代码量就增加了

私有格式
    __属性名
    __函数名
"""
class Prentice:
    def __init__(self):
        self.kongfu = "煎饼配方"
        self.__money = 10000

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼")

    #针对私有的属性 提供公共的访问方式
    def get_money(self):         #获取
        return self.__money
    #更改
    def set_money(self,money):   #设置
        self.__money = money

class TuSun(Prentice):
    pass

ts = TuSun()
print(ts.kongfu)
ts.make_cake()
print("-"*34)
#print(ts.__money)   #报错 父类私有成员 子类无法访问
ts.set_money(100)
print(ts.get_money())
