'''
演示 init 魔法方法的用法


魔法方法：
    是python内置函数 在满足特定的场景下 会被自动调用

    常用的魔法方法：
        __init__  在（每次）创建对象的时候 会自动出发改类的__init__()函数
        __str__
        __del__
'''

class Car:
    #魔法方法init()初始化 属性
    def __init__(self):
        print("我是无参 init 魔法方法")

        #在init方法中 初始化属性 则：该类所有对象 一创建 就有这些属性了
        self.color = "红色"
        self.number = 3

    #定义show()函数 打印该类对象的 各个属性
    def show(self):
        print(f"颜色{self.color} 轮胎数{self.number}")



c1 = Car()  #会自动调用 __init__()方法
#修改c1对象的属性
c1.color = "蓝色"
c1.number = 6
print(c1.color,c1.number)
c1.show()

print("-"*34)

c2 = Car()
c2.show()