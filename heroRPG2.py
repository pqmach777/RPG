#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random
from random import randrange
from random import randint
from random import uniform
    
class Character:
    def __init__(self,health,power):   
        self.name = ""
        self.health = health
        self.power = power
        self.player = True
        self.crit_chance = True
        self.coins = 100
        self.iteminventory = []
        self.armorinventory = []
        self.weaponinventory = []
        self.armor = 0 
        self.evade = 0


    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self,enemy):
        if self.player == True:
            if self.crit_chance == True: 
                if randint(1,5) == 5:
                    if self.name == "Hero-sama":
                        enemy.health -= float(self.power * 2)
                        print(f"{self.name} critical for {float(self.power*2)} damage to {enemy.name}.")
                    elif self.name == "Pasion the Beast King":
                        enemy.health -= float(self.power * 1.75)
                        print(f"{self.name} critical for {float(self.power*2)} damage to {enemy.name}.")                       
                    else:
                        enemy.health -= float(self.power * 1.5)
                        print(f"{self.name} critical for {float(self.power*1.5)} damage to {enemy.name}.")

                else:
                    enemy.health -= self.power
                    print(f"{self.name} did {self.power} damage to {enemy.name}.")
            else:
                enemy.health -= self.power
                print(f"{self.name} did {self.power} damage to {enemy.name}.")
            if enemy.name != "Zombie Lord" and enemy.health <= 0:
                print(f"{self.name} has slain {enemy.name}.")
                self.coins += enemy.bounty
                print(f"{self.name} have {self.money}")

        else:
            if self.crit_chance == True:
                if randint(1,5) == 5:                    
                    enemy.health -= float(self.power * 1.5)
                    print(f"{self.name} critical for {float(self.power*1.5)} damage to {enemy.name}.")
                else:
                    enemy.health -= self.power
                    print(f"{self.name} did {self.power} damage to {enemy.name}.")
            else:
                enemy.health -= self.power
                print(f"{self.name} did {self.power} damage to {enemy.name}.")
            if enemy.health <=0:
                print("You are dead.")

    def items_Inventory(self,enemy):
        print(f'Here is what in your item inventory: {self.iteminventory}')  
        use_item = input("What item would you like to use? ") 
        if use_item == "Super Tonic":
            self.iteminventory.remove(use_item)
            self.health += 10
            print(f'You have healed {self.health} health.')
        if use_item == "Scroll of Teleport" or self.player == True:
            self.evade += 2
            if self.evade > 0 :
                number = round(uniform(0.1,(1.0 - float(0.05 * self.evade)))2)
                if number != float(0.1) and number <= float(0.2):
                    print(f"{self.name} evaded {enemy.name} hit!")
                else:
                    self.attack(enemy)
            else:
                self.attack(enemy)
        else:
            self.attack(enemy)
                

                    

        
    def armor_Inventory(self,enemy):
        if use_armor == "Light Armor" or self.player == True:
            self.armor += 2
            if self.armor >= enemy.power:
                print(f'You tanked his hit.{self.name} received no damage.')
            else:
                self.health -= (enemy.power - self.armor)
                print(f"{enemy.name} did {enemy.power} damage to {self.name}.")    
        else:
            self.attack(enemy)
    




    def weapon_Inventory(self):

    def print_status(self):
        if self.player == True:
            print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")
        else: 
            print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")
        

class Hero(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Hero-sama"
        self.player = True
        self.crit_chance = True
        self.coins = 100
        self.armor = 0
        self.evade = 0

class Goblin(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Goblin"
        self.player = False
        self.crit_chance = True
        self.bounty = 10


class Zombie(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Zombie Lord"
        self.player = False
        self.crit_chance = True
        self.bounty = 20
    def alive(self):
            return True

class Medic(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Moira"
        self.player = True
        self.crit_chance = False
        self.money = 100
        self.armor = 0
        self.evade = 0
    def print_status(self):
        if randint(1,5) == 5:
            self.health += 2
            print(f"{self.name} healed for 2 health")
        print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")

class Shadow(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Naruto"
        self.player = True
        self.crit_chance = True
        self.money = 100
        self.armor = 0
        self.evade = 2
    def attack(self,enemy):
        if self.name == "Naruto" and randint(1,10) > 1:
            enemy.power = 0
            print(f"{self.name} uses Kage Bunshin no Jutsu. {enemy.name} killed some shadow clones.")
            super().attack(enemy)
        else:
            super().attack(enemy)

class Dragon(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Smaug"
        self.player = False
        self.crit_chance = True
        self.bounty = 500

class Beastman(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Pasion the Beast King"
        self.player = True
        self.crit_chance = True
        self.animalinstict = True
        self.money = 100
        self.armor = 0
        self.evade = 0

    def attack(self,enemy):
        if self.animalinstict == True and self.health <= 6:
            if randint(1,4) > 1:
                print(f"{self.name}'s animal instict has been activated. Damage is double at the cost of 1 health.")
                print(f"{self.name} lose 1 health point.")
                self.health -= 1
                enemy.health -= float(self.power*2)
                print(f"{self.name} did {self.power*2} damage to {enemy.name}.")
            else: 
                super().attack(enemy)           
        else:
            super().attack(enemy)

class Store:
    itemsStore = {
    'Super Tonic' : 15
    'Scroll of Teleportation' : 30
    }
    armorStore ={
    'Light Armor' : 50
    }
    weaponStore = {
    'Short Sword' : 50
    'Shield' : 50 
    'Great Sword' : 100
    }

    def purchase_items(self):
        shopping = input(f"Would {self.name} like to go shopping? (Yes/No) ")
        if shopping == 'Yes':
            buying_options = input("What do you want to buy? (Items, Armors, Weapons) ")
            if buying_options == 'Items':
                items_tobuy = input(f'What items would you like to buy? {}')



beastman = Beastman(12,5)
medic = Medic(8,2)    
hero = Hero(15,5)
goblin = Goblin(10,2)
zombielord = Zombie(10,1)
shadow = Shadow(1,4)
enemylist = [goblin,zombielord]
playerlist = [hero,medic,shadow,beastman]



def main(enemy):

    while enemy.alive() and beastman.alive():
        beastman.print_status()
        enemy.print_status()

        print()
        print("What do you want to do?")
        print(f"1. Fight {enemy.name}.")
        print("2. Do nothing.")
        print("3. Flee.")
        print("> ", end=' ')
        keyinput = input()
        if keyinput == "1":
            beastman.attack(enemy)
        elif keyinput == "2":
            pass
        elif keyinput == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {keyinput}")

        if enemy.alive():
            enemy.attack(beastman)
        
 

main(enemylist[randint(0, 1)])
