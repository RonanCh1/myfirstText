import random


class Character():
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.ap = 110

    def take_Dmg(self, dmg):
        self.hp -= dmg
        return self.hp

    def is_dead(self):
        if self.hp < 1:
            self.hp = 0
            return True,
        else:
            False


pc = Character()
dmg_amt = random.randint(0, pc.ap)
print("the pc took " + str(dmg_amt) + " Damage")
#print("the pc has",  ,"health")
print(f"the pc has {pc.take_Dmg(dmg_amt)} health ")
