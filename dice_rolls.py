from random import randint


def _4sided_dice_roll():
    return randint (1,4)
def _6sided_dice_roll():
    return randint (1,6)
def _8sided_dice_roll():
    return randint (1,8)
def _10sided_dice_roll():
    return randint (1,10)
def _20sided_dice_roll():
    return randint (1,20)
d4 = _4sided_dice_roll()
d6 = _6sided_dice_roll()
d8 = _8sided_dice_roll()
d10 = _10sided_dice_roll()
d20 = _20sided_dice_roll()
type_of_dice = input("What type of dice do you wanna roll?")
num_rolls = input("How many rolls?")
class roll():
     
    if type_of_dice == d4:
        for i in range (0,num_rolls):
            print _4sided_dice_roll()
    elif type_of_dice == d6:
        for i in range (0, num_rolls):
            print _6sided_dice_roll()
    elif type_of_dice == d8:
        for i in range (0,num_rolls):
            print _8sided_dice_roll()
    elif type_of_dice ==d10:
        for i in range (0,num_rolls):
            print _10sided_dice_roll()
    elif type_of_dice == d20:
        for i in range (0,num_rolls):
            print _20sided_dice_roll()
    else:
        print"Invaild. Try using d4, d6, d8, d10, d20 instead."



