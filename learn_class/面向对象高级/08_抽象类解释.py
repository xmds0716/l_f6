"""
抽象类：
    在python中 抽象类 = 接口  即：有抽象方法的类就是抽象类 也叫 接口
作用：
    抽象类一般充当父类 用于指定行业规范 准则 具体实现交由 子类 来完成
"""

class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class XiaoMi(AC):
    def cool_wind(self):
        print("小米制冷")
    def hot_wind(self):
        print("小米制热")
    def swing_l_r(self):
        print("小米左右摆头")

class Gree(AC):
    def cool_wind(self):
        print("格力制冷")

    def hot_wind(self):
        print("格力制热")

    def swing_l_r(self):
        print("格力左右摆头")

if __name__ == "__main__":
    xm = XiaoMi()
    xm.cool_wind()
    xm.hot_wind()
    xm.swing_l_r()
    print("-"*23)
    gree = Gree()
    gree.cool_wind()
    gree.hot_wind()
    gree.swing_l_r()