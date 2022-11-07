import random
import sys


class Character():
    def __init__(self,
                 name,
                 health="100",
                 attack="20",
                 mana="100",
                 stamina="50"):
        self.name = name
        self.hp = health
        self.ap = attack
        self.mp = mana
        self.stam = stamina

    def take_Dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 1:
            self.hp = 0
        return self.hp

    def get_atk(self, defense_roll):
        atk = random.randint(0, self.ap)

        if atk < defense_roll:
            atk = 0
        else:
            atk -= defense_roll
        return atk

    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False


class End_state():
      def __init__(self):
        print("ending")
        sys.exit()

class Story():
    def __init__(self):
        print("Welcome Traveler")
        self.new_game()

    def validate(self, question, answers):
      answer = " "
      while answer not in answers:
        print("please prov answer")
        answer  = input(question)

      return answer
    def new_game(self):
        self.create_character()

    def create_character(self):
        pc_name = input("Enter character name \n -> ")
        pc = Character(pc_name)
        self.outside(pc)

    def outside(self, pc):
        
        print("You stand here  ")
        print("cool sesond line that inspires ")
        print("really cool third line ")

        pc_input = self.validate("Enter?    \n ->",["yes","no"])
        if pc_input == "yes":
            print(f"yayayayaya {pc.name}")
            pass  #choices for player
        else:
            print("wawawa")


newgame = Story()
