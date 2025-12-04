'''
演示魔法方法 __init__ 有参数

__init__魔法方法 在创建对象的时候 会被自动调用 一般会给该类对象的 属性 进行初始化

————>无参：默认底色 需要重新涂色（覆盖底色)
     有参：
'''

class Car:
    #有参的 __init__ ()函数 参数值由外部对象自行赋值
    def __init__(self, color, number):
        """
        该魔法方法用于给Car类赋值
        :param color:  车的颜色
        :param number:  车的轮胎数
        """
        self.color = color
        self.number = number

    def show(self):
        print(f"颜色：{self.color} 轮胎数{self.number}")

#c1.Car()   报错 因为默认调用了init()函数 但是函数有参数 必须传参
c1 = Car("红色",4)
c1.show()

print("-"*23)

c2 = Car("绿色",6)
c2.show()

