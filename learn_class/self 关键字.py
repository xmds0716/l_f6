"""
谁调用函数  self就代表哪个对象
"""

#1.定义类
class Car:
    #属性

    #行为
    def run(self):
        print("汽车会跑")
        print(f"我是run函数 self的值是{self}")


#2.创建对象
c1 = Car()
print(f"c1对象是{c1}")
c1.run()

print("------------------------------------")

c2 = Car()
print(f"c2对象是{c2}")
c2.run()



























