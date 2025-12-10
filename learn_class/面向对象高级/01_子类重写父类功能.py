"""
重写解释：
    重写也叫覆盖 即：子类出现和父类重名的属性 或 行为   称之为 重写
调用层次：
    遵循 就近原则  子类有就用 没有就去父类找 依次查找所有父类 就有用 没有就报错
"""

class Master:
    def __init__(self):
        self.kongfu = "[古法配方]"

    def make_cake(self):
        print(f"采用{self.kongfu}制作煎饼")

class School:
    def __init__(self):
        self.kongfu = "[现代配方]"

    def make_cake(self):
        print(f"采用{self.kongfu}制作煎饼")

class Prentice(School,Master):
    def __init__(self):
        self.kongfu = "[独创配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}制作煎饼")

p = Prentice()
print(p.kongfu)
p.make_cake()