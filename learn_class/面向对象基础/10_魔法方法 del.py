
'''
演示 del 魔法方法的用法


魔法方法：
    是python内置函数 在满足特定的场景下 会被自动调用

    常用的魔法方法：
        __init__  在（每次）创建对象的时候 会自动出发改类的__init__()函数
        __str__   当用print()函数打印对象的时候 会自动调用该对象（所在类）的str魔法方法
                  该魔法方法默认打印的是对象的地址值 无意义 一般都会重写 改为打印 对象的各个属性值
        __del__   当.py文件执行结束 或者 手动del 释放对象资源 会自动调用该函数
'''

class Car:
    def __init__(self,brand):
        self.brand = brand

    def __str__(self):
        return f"品牌:{self.brand}"

    #删除对象时会给出提示
    def __del__(self):
        print(f"{self.brand}被删除了")

c1 = Car("Bmw")
print(c1)
print(c1.brand)

print("-"*23)

del c1
