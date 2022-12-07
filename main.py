import random
import sys
import time
from pprint import pprint


class Character():
    def __init__(self, c_hp, c_attack, c_luck, c_range, c_defense, c_mana, c_stamina, c_name):
      self.health = c_hp
      self.attack = c_attack
      self.luck = c_luck
      self.range = c_range
      self.defense = c_defense
      self.mana = c_mana
      self.stamina = c_stamina
      self.name = c_name
    
    def getHealth(self):
      return self.health
    def getAttack(self):
      return self.attack
    def getLuck(self):
      return self.luck
    def getRange(self):
      return self.range
    def getDefense(self):
      return self.defence
    def getMana(self):
      return self.mana
    def getStamina(self):
      return self.stamina
    def getName(self):
      return self.name
    
    def setHealth(self, new_Value):
      self.health = new_Value
    def setAttack(self, new_Value):
      self.attack = new_Value
    def setLuck(self, new_Value):
      self.luck = new_Value
    def setRange(self, new_Value):
      self.range = new_Value
    def setDefense(self, new_Value):
      self.defence = new_Value
    def setMana(self, new_Value):
      self.Mana = new_Value
    def setStamina(self, new_Value):
      self.stamina = new_Value
    def setName(self, new_Value):
      self.name = new_Value

class Enemy():
  def __init__(self ,e_health, e_attack, e_special_atk, e_hit_chance, e_name):
    self.health = e_health
    self.attack = e_attack
    self.special_atk = e_special_atk
    self.hit_chance = e_hit_chance
    self.name = e_name

  def getHealth(self):
    return self.health
  def getAttack(self):
    return self.attack
  def getSpecial_atk(self):
    return self.special_atk
  def getHit_chance(self):
    return self.hit_chance
  def getName(self):
    return self.name

  def setHealth(self, new_value):
    self.health = new_value
  def setAttack(self, new_value):
    self.attack = new_value
  def setSpecial_atk(self, new_value):
    self.special_atk = new_value
  def setHit_chance(self, new_value):
    self.hit_chance = new_value
  def setName(self, new_value):
    self.name = new_value

class Boss(Enemy):
  def __init__(self, e_health, e_attack, e_special_atk, e_hit_chance, e_name, e_ultimate_move):
    super().__init__(e_health, e_attack, e_special_atk, e_hit_chance, e_name)

    self.ultimate_move = e_ultimate_move

  def getUltimate(self):
   return self.ultimate_move

  def setUltimate(self, new_ultimate_move):
    self.ultimate_move = new_ultimate_move

  
  
def enemy_generator(level_boss):
  temp = []
  file = open("adjectives.txt", "r")
  lines = file.readlines()
  adjective = lines[random.randint(0,len(lines)-1)][:-1]
  file.close
  file = open("animals.txt", "r")
  lines = file.readlines()
  animals = lines[random.randint(0,len(lines)-1)][:-1]
  file.close


  if level_boss == False:
    health = random.randint(50,100)
    attack = random.randint(1,10)
    special = random.randint(2,20)
    chance = random.randint(1,10)

    return Enemy(health, attack, special, chance , adjective+ " "+ animals)

  else:
    health = random.randint(200,300)
    attack = random.randint(20,40)
    special = random.randint(50,90)
    chance = random.randint(1,8)
    ultimateMove = random.randint(100,200)

    return Boss(health, attack, special, chance , adjective+ " "+ animals, ultimateMove)

class Story():
    def __init__(self):
        print("Welcome Traveler")
        self.new_game()

    def validate(self, question, answers):
        answer = " "
        while answer not in answers:
            #print("please prov answer")
            answer = input(question)
        return answer

    def new_game(self):
        self.create_character()

    def create_character(self):
        pc_name = input("Enter character name \n -> ")
        pc = Character(pc_name)
        self.outside()

    def dead(self):
        print("You Died \n")
        pc_input = self.validate("Do you wish to start a new game",
                                 ["yes", "no"])
        if pc_input == "yes":
            self.new_game
        else:
            sys.exit()

    def outside(self):

        print("You stand here upon a tall spiked gate ")
        print("you see the the bones of the fallen surrounding the gate ")

        pc_input = self.validate(" Do you open the gate?    \n ->",
                                 ["yes", "no"])
        if pc_input == "yes":
            print(" The Gate opens  /n")
            print("you have passed the gate")
            self.courtyard()
        else:
            print("You have chosen not to open the gate")
            print("You have been added to the bones of the fallen")
            self.dead()

    def courtyard(self):
        print("You stumbled upon a building ")
        print("Do you Enter? ")
        print("OR Shall you take the trail ")

        pc_input = self.validate("What Path have you chosen  \n ->",
                                 ["yes", "no", "trail"])
        if pc_input == "yes":
            print("you have chosen to enter the building ")
        elif pc_input == "no":
            print("you have chosen not to enter the house")
        elif pc_input == "trail":
            print("you have chosen to take the trail")


#newgame = Story()          
def create_class():
  response = input("Are you more Strat(1) or more of a Warrior(2)...")
  while response != "1" and response != "2":
   print("Invalid")
   response = input("Are you more Strat(1) or more of a Warrior(2)...")
  if response == "1":
    charAttack = 50
    charDefense = 100
    charStamina = 50
  elif response == "2":
    charAttack = 100
    charDefense = 50
    charStamina = 100
  response = input("Press Enter to roll dice...")
  time.sleep(0.2)
  print("Rolling Dice ")
  time.sleep(0.2)
  charLuck = random.randint(0, 20)
  print(f"Your Character has {charLuck} luck out of 20")

  response = input("Are you more of an Marksman(1) or a magic user(2) ")

  while response != "1" and response != "2":
   print("Invalid")
   response = input("Are you more of an Marksman(1) or a magic user(2)...")
  if response == "1":
    charRange = 100
    charMana = 30
  elif response == "2":
    charRange = 50
    charMana = 100
  charName = input("What is your name stranger ")
  print(f"Welcome {charName} ")

  return (charAttack, charLuck, charRange, charDefense, charMana, charStamina, charName)

class_attribute = create_class()
player = Character(100, class_attribute[0], class_attribute[1], class_attribute[2], class_attribute[3], class_attribute[4], class_attribute[5], class_attribute[6])

level_boss = False
en1 = enemy_generator(level_boss)
en2 = enemy_generator(level_boss)
en3 = enemy_generator(level_boss)
pprint(vars(en1))
pprint(vars(en2))
pprint(vars(en3))
