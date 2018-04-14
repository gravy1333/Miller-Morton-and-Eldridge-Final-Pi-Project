from random import randint
High = input("What is your highest character level?")
low = input("What is your lowest character level?")

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

if High <= 10 and low >= 0:
    type_of_dice = d4
    num_rolls = 1
elif High <= 15 and low >=0:
    type_of_dice = d6
    num_rolls =1
elif High <=20 and low >= 0:
    type_of_dice = d8
    num_rolls = 1
elif High <= 25 and low >= 0:
    type_of_dice = d10
    num_rolls = 1
elif High <= 30 and low >=10:
    type_of_dice = d4
    num_rolls = 2
elif High <=30 and low >= 15:
    type_of_dice = d6
    num_rolls = 2
elif High <= 30 and low >= 20:
    type_of_dice = d8
    num_rolls = 2
elif High <= 30 and low >= 25:
    type_of_dice = d10
    num_rolls = 2
elif High == 30 and low == 30:
    type_of_dice = d20
    num_rolls = 2
elif High == 100 and low == 100:
    type_of_dice = d20
    num_rolls = 6
else:
    type_of_dice = d20
    num_rolls = 3
    


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



    


        


