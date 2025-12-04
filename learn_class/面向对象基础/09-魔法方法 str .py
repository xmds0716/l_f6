'''
演示 str 魔法方法的用法


魔法方法：
    是python内置函数 在满足特定的场景下 会被自动调用

    常用的魔法方法：
        __init__  在（每次）创建对象的时候 会自动出发改类的__init__()函数
        __str__   当用print()函数打印对象的时候 会自动调用该对象（所在类）的str魔法方法
                  该魔法方法默认打印的是对象的地址值 无意义 一般都会重写 改为打印 对象的各个属性值
        __del__
'''
class Car:
    def __init__(self,color,number):
        self.color = color
        self.number = number

    def __str__(self):
        #return "字符串"   该魔法方法默认打印的是对象的地址值 无意义 一般都会重写 改为打印 对象的各个属性值
        return f"颜色{self.color} 车轮数{self.number}"

c1 = Car("绿色",4)
print(c1)

print("-"*23)

c2 = Car("红色",6)
print(c2)