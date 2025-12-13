"""
案例：演示python的多态案例
需求
    1.构建对战平台object_plau()  接收： 英雄机 敌机
    2.在不修改对战平台代码的情况下 完成多次战斗
    3.规则
        英雄机：一代战斗力60 二代战斗力80
        敌机 ： 战斗力70

英雄一代  HeroFigher
英雄一代  AdvHeroFigher
敌机     EnemyFighter
"""

class HeroFigher:
    def power(self):
        return 60

class AdvHeroFigher(HeroFigher):
    def power(self):
        return 80

class EnemyFighter:
    def power(self):
        return 70

#对战平台
def object_play(hero:HeroFigher,enemy:EnemyFighter): #不加类型
    if hero.power() > enemy.power():
        print("胜利")
    else:
        print("失败")

if __name__ == '__main__':
    #不使用多态
    '''
    h1 = HeroFigher()
    e1 = EnemyFighter()
    if h1.power() > e1.power():
        print("战胜")
    else:
        print("失败")
    h2 = AdvHeroFigher()

    if h2.power() > e1.power():
        print("胜利")
    else:
        print("失败")
     '''

    #使用多态
    h1 = HeroFigher()
    h2 = AdvHeroFigher()
    e1 = EnemyFighter()

    object_play(h1,e1)
    object_play(h2,e1)
    object_play(h2,h1) #h1警告 可以不加类型