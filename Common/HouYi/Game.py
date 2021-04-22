from Portal_interface.Common.Game.Game import Game
class HouYi(Game):
    ##如果在子类重新定义了_init__，那么父类的_init_将会被覆盖
    def __init__(self):
        super().__init__(1000,200)
        self.defence = 100

    def houyi_fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp + self.defence - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            if self.hp <= 0:
                print("我输了！")
                break
            elif enemy_hp <= 0:
                print("我赢了！")
                break
            # else:
            #     raise Exception("没有平局！！！")

hp = 1000
power = 300
houyi = HouYi()
houyi.houyi_fight(hp,power)