"""
继承概述：
    子类可以继承父类的属性 和 行为
    #子承父业
写法：
    class 子类名(父类名):
        pass
例：
    class A(B):
        pass
叫法：
    A: 子类 派生类
    B: 父类  基类 超类
好处：
    提高代码的复用性
弊端：
    耦合性增强 父类不好的内容 子类想没有都不行
扩展：开发原则
    高内聚 低耦合
    内聚：类自己独立处理问题的能力
    耦合：类与类之间的关系
    #自己能搞定 不要依赖别人
"""

class Father(object):
    def __init__(self):
        self.gender = '男'

    def walk(self):
        print("走路")

class Son(Father):
    pass

s = Son()
print(f"{s.gender}")
s.walk()