#Random monster generator
from monsters import *
import random
from random import randint

party_size = input("How big is your party")
def monster_spawn(party_size):
    number_of_monsters = 0
    if party_size == 1:
        number_of_monsters = randint(1,2)
        print number_of_monsters
        monster = random.choice(Monster_Dictionary.keys())
        print monster
        print Monster_Dictionary[monster]
    elif party_size == 2:
        number_of_monsters = randint(1,2)
        print number_of_monsters
        monster = random.choice(Monster_Dictionary.keys())
        print monster
        print Monster_Dictionary[monster]
    elif party_size == 3:
        number_of_monsters = randint(2,3)
        print number_of_monsters
        monster = random.choice(Monster_Dictionary.keys())
        print monster
        print Monster_Dictionary[monster]
    elif party_size == 4:
        number_of_monsters = randint(3,4)
        print number_of_monsters
        monster = random.choice(Monster_Dictionary.keys())
        print monster
        print Monster_Dictionary[monster]
    elif party_size == 5:
        number_of_monsters = randint(4,5)
        print number_of_monsters
        monster = random.choice(Monster_Dictionary.keys())
        print monster
        print Monster_Dictionary[monster]
    
monster_spawn = monster_spawn(party_size)
