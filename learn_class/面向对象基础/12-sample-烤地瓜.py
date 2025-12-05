'''
1.定义地瓜类 -> SweetPotato
2.属性：被烤时间cook_time 烘焙状态cook_state 调料condiments
3.行为：烘烤cook() 添加调料add_condiments()
4.魔法方法：init() -> 初始化  str() -> 打印地瓜信息
5.规则：
    烘烤时间      地瓜状态
    [0,3)         生的
    [3,7)         半生不熟
    [7,12)        熟了
    [12，∞)       烤糊了
'''
class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = "生的"
        self.condiments = []

    def cook(self,time):
        if time < 0:
            print("不合法")
        else:
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_state = "生的"
            elif 3 <= self.cook_time < 7:
                self.cook_state = "半生不熟"
            elif 7 <= self.cook_time < 12:
                self.cook_state = "熟了"
            else:
                self.cook_state = "烤糊了"

    def add_condiments(self,condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return f"烘烤时间{self.cook_time}分钟 地瓜状态：{self.cook_state} 调料：{self.condiments}"

# 测试代码
if __name__ == '__main__':
    dg = SweetPotato()

    #烘烤动作
    dg.cook(5)
    #添加调料
    dg.add_condiments("盐,番茄酱")
    dg.add_condiments("折耳根")
    #打印状态
    print(dg)
