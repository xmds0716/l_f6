"""
多态：
    同一个函数 接收不同的参数 有不同的效果
    #同一个事物在不同时刻表现出来的不同状态 形态

前提条件：
    1，要有继承
    2，要有方法重写 不然多态无意义
    3，要有父类引用指向子类对象  an:Animal = Dog()
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("狗叫")

class Cat(Animal):
    def speak(self):
        print("猫叫")

class Car:
    def speak(self):
        print("车叫")

#定义函数 接收不同的动物对象 调用speak方法
def make_speak(an:Animal):
    an.speak()

if __name__ == '__main__':
    #an:Animal = Dog()   #父类引用指向子类对象
    d = Dog()
    c = Cat()
    car = Car()

    #演示多态
    make_speak(d)
    make_speak(c)

    #测试汽车和
    make_speak(car)