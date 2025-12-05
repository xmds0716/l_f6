'''
体重100kg 每跑步一次 减重0.5kg 每吃喝一次 增重2kg
'''

class Student:
    def __init__(self):
        self.weight = 100

    def run(self):
        print("跑步..")
        self.weight -= 0.5

    def eat(self):
        print("吃喝..")
        self.weight += 2

    #重写魔法方法 str 打印属性
    def __str__(self):
        return f"体重是{self.weight}kg"


if __name__ == '__main__':
    xm = Student()

    #跑步
    xm.run()

    #吃喝
    xm.eat()

    #当前体重
    print(xm)