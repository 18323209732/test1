class Game:

    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了！")
        elif final_hp < enemy_final_hp:
            print("敌人赢了！")
        else:
            print("平局")