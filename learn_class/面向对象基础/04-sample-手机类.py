"""
定义手机类 能开机 关机 拍照

定义类
    class 类名:
        #属性
        #行为

    访问 类中成员
        类外：对象名.
        类内：self.
"""

class Phone:
    #属性

    #行为
    def open(self):
        print(f"{self}手机开机了")

    def close(self):
        print(f"{self}手机关机了")

    def take_photo(self):
        print(f"{self}手机拍照了")

p1 = Phone()
print(f'p1对象是{p1}')
p1.open()
p1.take_photo()
p1.close()

print("="*34)

p2 = Phone()
print(f'p2对象是{p2}')
p2.open()
p2.take_photo()
p2.close()
