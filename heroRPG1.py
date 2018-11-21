#!/usr/bin/env python

# In this simple RPG game, the hero fights the Zombie Lord or goblin. He has the options to:

# 1. Figh Zombie Lord or globlin.
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
    
class Character:
    def __init__(self,health,power):   
        self.name = ""
        self.health = health
        self.power = power
        self.player = True
    def alive(self):
        if self.health > 0 or self.name == "Zombie Lord":
            return True
        else:
            return False

    def attack(self,enemy):
        if self.player == True:
            enemy.health -= self.power
            print(f"{self.name} did {self.power} damage to {enemy.name}.")
            if  enemy.name != "Zombie Lord" and enemy.health <= 0:
                print(f"{self.name} has slain {enemy.name}.")
        else:
            enemy.health -= self.power
            print(f"{self.name} did {self.power} damage to {enemy.name}.")
            if enemy.health <=0:
                print("You are dead.")

    def print_status(self):
        if self.player == True:
            print(f"{self.name} health: {self.health}, {self.name} power: {self.power}")
        else: 
            print(f"The {self.name} health: {self.health}, {self.name} power: {self.power}")
        

class Hero(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Hero-sama"
        self.player = True



class Goblin(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Goblin"
        self.player = False

class Zombie(Character):
    def __init__(self,health,power):
        super().__init__(health,power)
        self.name = "Zombie Lord"
        self.player = False
    def alive(self):
        return True
      

def main():
    the_hero = Hero(10,5)
    the_goblin = Goblin(6,2)
    the_zombielord = Zombie(10,1)
    monster1 = the_goblin
    monster2 = the_zombielord

    while the_hero.alive():
        the_hero.print_status()
        # the_goblin.print_status()
        the_zombielord.print_status()
        print()
        print("What do you want to do?")
        print(f"1. Fight {the_zombielord.name}.")
        print("2. Do nothing.")
        print("3. Flee.")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            the_hero.attack(the_zombielord)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if monster2.health > 0:
            monster2.attack(the_hero)
        
 

main()

      
