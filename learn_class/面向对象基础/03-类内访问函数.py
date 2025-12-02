'''
self关键字：
    代表本类当前对象的引用 谁调用 self代表谁

    用于函数区分不同对象

总结：
    1.在 类外 访问类中的行为 需要通过 对象名. 的方式访问
    2.在 类内 访问类中的行为 需要通过 self. 的方式访问
    3.类内的self = 类外的对象名
'''

class Car:
    #属性

    #行为
    def run(self):
        print(f"{self}汽车在跑")

    def work(self):
        print(f"我是work 我的self{self}")
        self.run() #本类当前对象的引用

#在类外访问Car类的行为（函数）
c1 = Car()
print(f"c1对象:{c1}")
c1.run()
print("-"*34)
c1.work()

print("="*34)

#再次创建对象那边
c2 = Car()
print(f"c2对象:{c2}")
c2.run()
print("-"*34)
c2.work()

