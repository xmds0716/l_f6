"""
1.父类名.父类函数名(self)    精准访问 想找哪个父类 就调哪个父类
2.super().父类函数名()      只能访问最近的一个父类 有就用 没有就往后查找
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

    #def make_master_cake(self):
    #    Master.__init__(self)
    #    Master.make_cake(self)

    #def make_school_cake(self):
    #    School.__init__(self)
    #    School.make_cake(self)

    def make_old_cake(self):
        super().__init__()
        super().make_cake()

p = Prentice()
print(p.kongfu)
p.make_cake()
#p.make_master_cake()
#p.make_school_cake()
print("-"*34)
p.make_old_cake()