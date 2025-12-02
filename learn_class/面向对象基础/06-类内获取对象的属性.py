'''
回顾：
    1.类外访问类中的成员 可以通过 对象名. 的方式
    2.类内访问类中的成员 可以通过 self. 的方式
    3.类外通过 对象名.属性名 = 属性值 的方式 设置对象的属性 只有当前对象有

类内如何设置属性： 要结合 魔法方法 __init__()来实现
'''

class Car:
    #属性

    #行为
    def run(self):
        print("汽车在跑")

    def show(self):
        print(f"我是show函数 对象颜色：{self.color} 轮胎数：{self.num}")

c1 = Car()
#类外设置属性
c1.color = "红色"
c1.num = 4
#类外访问属性
print(f"颜色{c1.color},轮胎数{c1.num}")

#类外访问行为
c1.run()
c1.show()

print("-"*34)

c2 = Car()
c2.run()
#c2.show()   #报错

