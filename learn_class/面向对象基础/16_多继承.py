"""
扩展：MRO机制：
     解释：
         pyhton中有MRO机制 可以查看先找哪个类 后找哪个类
     格式：
         类名.mro()
         类名.__mro__
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

class Prentice(School,Master): #就近继承
    pass

xm = Prentice()
print(xm.kongfu)
xm.make_cake()

print("-"*23)

#查看mro机制
print(Prentice.mro())    #Prentice -> School -> Master -> object
print(Prentice.__mro__)  #Prentice -> School -> Master -> object