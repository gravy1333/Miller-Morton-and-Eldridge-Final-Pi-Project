from tkinter import *
import random
from random import randint
#from Health_LED import *
from player import *
from monsters import *

class Screen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        for i in range(8):
            master.columnconfigure(i, weight=1)
        master.rowconfigure(0, weight=3)
        master.rowconfigure(4, weight=2)
        master.rowconfigure(6, weight=0)
        master.rowconfigure(7, weight=1)
        self.grid(sticky='news')
        window.grid_propagate(0)

    def setGUI(self):
        #player health
        self.PLH = Label(window, bg='white', width=int(WIDTH/2))
        self.PLH.grid(row=0, column=0, rowspan=3, columnspan=4, sticky='news')
        
        self.PL1N = Label(self.PLH, text='player 1', bg='white', width=int(WIDTH/3))
        self.PL1N.grid(row=0, column=0, sticky='news')
        self.PL1L = Label(self.PLH, text=str(p1), fg='red', bg='black', width=int(WIDTH/6))
        self.PL1L.grid(row=0, column=1, sticky='news')

        self.PL2N = Label(self.PLH, text='player 2', bg='white', width=int(WIDTH/3))
        self.PL2N.grid(row=1, column=0, sticky='news')
        self.PL2L = Label(self.PLH, text=str(p2), fg='red', bg='black', width=int(WIDTH/6))
        self.PL2L.grid(row=1, column=1, sticky='news')

        self.PL3N = Label(self.PLH, text='player 3', bg='white', width=int(WIDTH/3))
        self.PL3N.grid(row=2, column=0, sticky='news')
        self.PL3L = Label(self.PLH, text=str(p3), fg='red', bg='black', width=int(WIDTH/6))
        self.PL3L.grid(row=2, column=1, sticky='news')

        self.PL4N = Label(self.PLH, text='player 4', bg='white', width=int(WIDTH/3))
        self.PL4N.grid(row=3, column=0, sticky='news')
        self.PL4L = Label(self.PLH, text=str(p4), fg='red', bg='black', width=int(WIDTH/6))
        self.PL4L.grid(row=3, column=1, sticky='news')

        self.PL5N = Label(self.PLH, text='player 5', bg='white', width=int(WIDTH/3))
        self.PL5N.grid(row=4, column=0, sticky='news')
        self.PL5L = Label(self.PLH, text=str(p5), fg='red', bg='black', width=int(WIDTH/6))
        self.PL5L.grid(row=4, column=1, sticky='news')

        for r in range(5):
            self.PLH.rowconfigure(r, weight=2)
        self.PLH.columnconfigure(0, weight=2)
        self.PLH.columnconfigure(1, weight=1)

        #Out box 
        self.out = Label(window, text='(Enter in input text bar)\nHow big is your party \nmembers #', \
                         anchor='nw', relief='sunken', justify='left', width=int(WIDTH/2), \
                         wraplength=int(WIDTH/2) -5, height=6)
        self.out.grid(row=4, column=0, rowspan=2, columnspan=4, sticky='news')

        #monster stats
        self.MA = Label(window, text='Awaiting Battle', anchor='nw', relief='sunken', \
                        justify='left', width=int(WIDTH/2), wraplength=int(WIDTH/2) -5)
        self.MA.grid(row=0, column=4, rowspan=3, columnspan=4, sticky='news')

        #monster actions
        self.Mstats = Label(window, text='Moster Actions', anchor='nw', relief='sunken', \
                            justify='left', width=int(WIDTH/2), wraplength = int(WIDTH/2) - 5)
        self.Mstats.grid(row=4, column=4, rowspan=2, columnspan=4, sticky='news')

        #input bar
        GW.player_input = Entry(window, bg='white')
        GW.player_input.bind("<Return>", GW.text_process)
        GW.player_input.grid(row=6, column=0, columnspan=8, sticky='we')
        GW.player_input.focus()
        
        #dice buttons
        self.RDis = Label(window, text='00', bg='white', width=int(WIDTH/8))
        self.RDis.grid(row=7, column=7, sticky='news')
        
        self.d4 = Button(window, bg='white', text='d4', width=int(WIDTH/8))
        self.d4.grid(row=7, column=0, sticky='news')
    
        self.d6 = Button(window, bg='white', text='d6', width=int(WIDTH/8))
        self.d6.grid(row=7, column=1, sticky='news')
        
        self.d8 = Button(window, bg='white', text='d8', width=int(WIDTH/8))
        self.d8.grid(row=7, column=2, sticky='news')
        
        self.d10 = Button(window, bg='white', text='d10', width=int(WIDTH/8))
        self.d10.grid(row=7, column=3, sticky='news')
        
        self.d12 = Button(window, bg='white', text='d12', width=int(WIDTH/8))
        self.d12.grid(row=7, column=4, sticky='news')
        
        self.d20 = Button(window, bg='white', text='d20', width=int(WIDTH/8))
        self.d20.grid(row=7, column=5, sticky='news')

        self.dRand = Button(window, bg='white', text='Random\nDice', \
                              width=int(WIDTH/8), command=self.randRoll)
        self.dRand.grid(row=7, column=6, sticky='news')

        self.d4['command'] = lambda val = 4 : self.roll(4)
        self.d6['command'] = lambda val = 6 :self.roll(6)
        self.d8['command'] = lambda val = 8 : self.roll(8)
        self.d10['command'] = lambda val = 10 : self.roll(10)
        self.d12['command'] = lambda val = 12 : self.roll(12)
        self.d20['command'] = lambda val = 20 : self.roll(20)
        self.dRand.bind('<7>', self.randRoll)

    def text_process(self, event):
        action = GW.player_input.get()
        action = action.lower()
        words = action.split()
        GW.player_input.delete(0, END)
        response = " I don't understand try 'valid commands' to view vaild commands."
        # the text box understands two commands
        if (len(words) == 2):
            verb = words[0]
            noun = words[1]
            if (verb == "valid"):
                if (noun == "commands"):
                    t = "To set health type 'set, player, [the player #], health, [player's health]\n"
                    t += "To attack a player type 'attack, player, [the player #], [the amount of damage]\n"
                    t += "To set the max health type 'set, max, health, player, [the player #], [the max health]\n"
                    t += "To set members type ' members, [# of members]\n"
                    t += "To spawn monsters type ' spawn, monsters'"
                    response = t
            elif (words[0] == "members"):
                self.party_size = int(words[1])
                response = "Party sized changed"
            elif (verb == "spawn"):
                if (noun == "monsters"):
                    GW.monster_spawn()
                    response = "Monsters spawn"
        # the text box understand three commands
        # the text box understands four word commands
        elif (len(words) == 4):
            verb = words[0]
            noun = words[1]
            number1 = int(words[2])
            number2 = int(words[3])
            if (verb == "attack"):
                if (noun == "player"):
                    if (number1 == 1):
                        p1.currentH += -number2
                        self.PL1L['text'] = str(p1)
                    elif (number1 == 2):
                        p2.currentH -= number2
                        self.PL2L['text'] = str(p2)
                    elif (number1 == 3):
                        p3.currentH -= number2
                        self.PL3L['text'] = str(p3)
                    elif (number1 == 4):
                        p4.currentH -= number2
                        self.PL4L['text'] = str(p4)
                    elif (number1 == 5):
                        p5.currentH -= number2
                        self.PL5L['text'] = str(p5)
                    response = "Player Health Changed"
                    #HealthDisplay(number1, players[number1 - 1])

        # the text box understands five word commands
        elif (len(words) == 5):
            verb = words[0]
            noun = words[1]
            number1 = int(words[2])
            noun2 = words[3]
            number2 = int(words[4])
            if (verb == "set"):
                if noun == "player":
                    if noun2 == "health":
                        if  number1 == 1:
                            p1.currentH = number2
                            self.PL1L['text'] = str(p1)
                        elif number1 == 2:
                            p2.currentH = number2
                            self.PL2L['text'] = str(p2)
                        elif number1 == 3:
                            p3.currentH = number2
                            self.PL3L['text'] = str(p3)
                        elif number1 == 4:
                            p4.currentH = number2
                            self.PL4L['text'] = str(p4)
                        elif number1 == 5:
                            p5.currentH = number2
                            self.PL5L['text'] = str(p5)
                        response = "Player Health Changed"
                        #HealthDisplay(number1, players[number1 - 1])
                        
        # the text box understand six words
        elif (len(words) == 6):
            verb = words[0]
            noun = words[1]
            noun2 = words[2]
            noun3 = words[3]
            number1 = int(words[4])
            number2 = int(words[5])
            if (verb == "set"):
                if (noun == "max"):
                    if (noun2 == "health"):
                        if (noun3 == "player"):
                            if (number1 == 1):
                                p1.maxH = number2
                                p1.currentH = number2
                                self.PL1L['text'] = str(p1)
                            elif (number1 == 2):
                                p2.maxH = number2
                                p2.currentH = number2
                                self.PL2L['text'] = str(p2)
                                
                            elif (number1 == 3):
                                p3.maxH = number2
                                p3.currentH = number2
                                self.PL3L['text'] = str(p3)
                            elif (number1 == 4):
                                p4.maxH = number2
                                p4.currentH = number2
                                self.PL4L['text'] = str(p4)
                            elif (number1 == 5):
                                p5.maxH = number2
                                p5.currentH = number2
                                self.PL5L['text'] = str(p5)
                            response = "Player Health Changed"
                            #HealthDisplay(number1, players[number1 - 1])
                            
        GW.out['text'] = "{}".format(response)

        
    def play(self):
        self.setGUI()

    def roll(self, val):
        roll = randint(1, val)
        self.RDis['text'] = roll
        
    def randRoll(self):
        die = diceVals[randint(1, 6)]
        self.roll(die)

    def monster_spawn(self):
        if self.party_size == 1:
            number_of_monsters = randint(1,2)
        elif self.party_size == 2:
            number_of_monsters = randint(1,2)
        elif self.party_size == 3:
            number_of_monsters = randint(2,3)
        elif self.party_size == 4:
            number_of_monsters = randint(3,4)     
        elif self.party_size == 5:
            number_of_monsters = randint(4,5)
        else:
            number_of_monsters = randint(4,5)
        monster = random.choice(list(Monster_Dictionary))
        GW.MA['text'] = "Number of Monsters: {} Name of Monster : {}".format(number_of_monsters,monster)
        GW.Mstats['text'] = "Monster's sheet reference [ Stats, Challenge Rating number,\n"
        GW.Mstats['text'] += "Experience points, Armor Class, Hp, Specs, Actions]\n"
        GW.Mstats['text'] += "Monster's sheet {}".format(Monster_Dictionary[monster])

#IMPORTANT DO NOT MESS WITH THIS
diceVals = [0, 4, 6, 8, 10, 12, 20]

p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
p5 = Player()
players = [p1, p2, p3, p4, p5]


#for index in range(0, len(players)):
    #HealthDisplay(index + 1, players[index])


m1 = Monster()
m2 = Monster()
m3 = Monster()
m4 = Monster()
m5 = Monster()
monsters = [m1, m2, m3, m4, m5]

WIDTH = 800
HEIGHT = 600

window = Tk()
window.title('DnD Dungen Master Tool for levels 0-1')
window.geometry('{}x{}'.format(WIDTH, HEIGHT))

GW = Screen(window)
GW.play()

window.mainloop()


""" for element in LED:
    LED[element].stop()
GPIO.cleanup() """
