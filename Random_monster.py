#Random monster generator
from monsters import *
from random import randint
import random

party_size = input("How big is your party: ")
print "Monster's sheet reference [ Stats, Challenge Rating number, Experience points, Armor Class, Hp, Specs, Actions]"
def monster_spawn(party_size):
    number_of_monsters = 0
    if party_size == 1:
        number_of_monsters = randint(1,2)
        monster = random.choice(Monster_Dictionary.keys())
        print "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        print"Monster's sheet {}".format(Monster_Dictionary[monster])
    elif party_size == 2:
        number_of_monsters = randint(1,2)
        monster = random.choice(Monster_Dictionary.keys())
        print "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        print"Monster's sheet {}".format(Monster_Dictionary[monster])
    elif party_size == 3:
        number_of_monsters = randint(2,3)
        monster = random.choice(Monster_Dictionary.keys())
        print "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        print"Monster's sheet {}".format(Monster_Dictionary[monster])
    elif party_size == 4:
        number_of_monsters = randint(3,4)     
        monster = random.choice(Monster_Dictionary.keys())
        print "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        print"Monster's sheet {}".format(Monster_Dictionary[monster])
    elif party_size == 5:
        number_of_monsters = randint(4,5)
        monster = random.choice(Monster_Dictionary.keys())
        print "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        print"Monster's sheet {}".format(Monster_Dictionary[monster])
    else:
        number_of_monsters = randint(4,5)
        monster = random.choice(Monster_Dictionary.keys())
        print "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        print"Monster's sheet {}".format(Monster_Dictionary[monster])
monster_spawn = monster_spawn(party_size)
