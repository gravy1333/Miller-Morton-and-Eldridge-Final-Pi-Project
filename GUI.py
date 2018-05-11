from Tkinter import *
from random import randint
#from Health_LED import *
from player import *
from Random_monster import *

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

    def setGUI(self):
        #player health
        self.PLH = Label(window, bg='white')
        self.PLH.grid(row=0, column=0, rowspan=3, columnspan=4, sticky='news')
        
        self.PL1N = Label(self.PLH, text='player 1', bg='white')
        self.PL1N.grid(row=0, column=0, sticky='news')
        self.PL1L = Label(self.PLH, text=str(p1), fg='red', bg='black')
        self.PL1L.grid(row=0, column=1, sticky='news')

        self.PL2N = Label(self.PLH, text='player 2', bg='white')
        self.PL2N.grid(row=1, column=0, sticky='news')
        self.PL2L = Label(self.PLH, text=str(p2), fg='red', bg='black')
        self.PL2L.grid(row=1, column=1, sticky='news')

        self.PL3N = Label(self.PLH, text='player 3', bg='white')
        self.PL3N.grid(row=2, column=0, sticky='news')
        self.PL3L = Label(self.PLH, text=str(p3), fg='red', bg='black')
        self.PL3L.grid(row=2, column=1, sticky='news')

        self.PL4N = Label(self.PLH, text='player 4', bg='white')
        self.PL4N.grid(row=3, column=0, sticky='news')
        self.PL4L = Label(self.PLH, text=str(p4), fg='red', bg='black')
        self.PL4L.grid(row=3, column=1, sticky='news')

        self.PL5N = Label(self.PLH, text='player 5', bg='white')
        self.PL5N.grid(row=4, column=0, sticky='news')
        self.PL5L = Label(self.PLH, text=str(p5), fg='red', bg='black')
        self.PL5L.grid(row=4, column=1, sticky='news')

        for r in range(5):
            self.PLH.rowconfigure(r, weight=2)
        self.PLH.columnconfigure(0, weight=2)
        self.PLH.columnconfigure(1, weight=1)


        #Out box 
        self.PLA = Label(window, text='Output box', anchor='nw', relief='sunken')
        self.PLA.grid(row=4, column=0, rowspan=2, columnspan=4, sticky='news')

        #player actions
        self.out = Label(window, text='Output box', anchor='nw', relief='sunken')
        self.out.grid(row=4, column=0, rowspan=2, columnspan=4, sticky='news')


        #monster stats
        self.stats = Label(window, text='Awaiting Battle', anchor='nw', relief='sunken')
        self.stats.grid(row=0, column=4, rowspan=3, columnspan=4, sticky='news')

        #monster actions
        self.MA = Label(window, text='Moster Actions', anchor='nw', relief='sunken')
        self.MA.grid(row=4, column=4, rowspan=2, columnspan=4, sticky='news')

        #input bar
        GW.player_input = Entry(window, bg='white')
        GW.player_input.bind("<Return>", GW.text_process)
        GW.player_input.grid(row=6, column=0, columnspan=8, sticky='we')
        GW.player_input.focus()
        
        #dice buttons
        self.RDis = Label(window, text='0', bg='white')
        self.RDis.grid(row=7, column=7, sticky='news')
        
        self.d4 = Button(window, bg='white', text='d4', width=1)
        self.d4.grid(row=7, column=0, sticky='news')
    
        self.d6 = Button(window, bg='white', text='d6', width=1)
        self.d6.grid(row=7, column=1, sticky='news')
        
        self.d8 = Button(window, bg='white', text='d8', width=1)
        self.d8.grid(row=7, column=2, sticky='news')
        
        self.d10 = Button(window, bg='white', text='d10', width=1)
        self.d10.grid(row=7, column=3, sticky='news')
        
        self.d12 = Button(window, bg='white', text='d12', width=1)
        self.d12.grid(row=7, column=4, sticky='news')
        
        self.d20 = Button(window, bg='white', text='d20', width=1)
        self.d20.grid(row=7, column=5, sticky='news')

        self.dRand = Button(window, bg='white', text='Random\nDice', \
                              width=1, command=self.randRoll)
        self.dRand.grid(row=7, column=6, sticky='news')

        self.d4['command'] = lambda val = 4 : self.roll(4)
        self.d6['command'] = lambda val = 6 :self.roll(6)
        self.d8['command'] = lambda val = 8 : self.roll(8)
        self.d10['command'] = lambda val = 10 : self.roll(10)
        self.d12['command'] = lambda val = 12 : self.roll(12)
        self.d20['command'] = lambda val = 20 : self.roll(20)
        self.dRand.bind('<7>', self.randRoll())
        self.RDis['text'] = '0'
        
    def text_process(self, event):
        print "Hello"
        action = GW.player_input.get()
        action = action.lower()
        words = action.split()
        GW.player_input.delete(0, END)
        # the text box understands four word commands
        if (len(words) == 4):
            verb = words[0]
            noun = words[1]
            number = words[2]
            number2 = words[3]
            response = " I don't understand try again."
            if (verb == attack):
                if (noun == player):
                    if (number == 1):
                        pass
                    if (number == 2):
                        pass
                    if (number == 3):
                        pass
                    if (number == 4):
                        pass
                    if (number == 5):
                        pass
            
        # the text box understands five word commands
        elif (len(words) == 5):
            verb = words[0]
            noun = words[1]
            number = words[2]
            noun2 = words[3]
            number2 = words[4]
            response = "I don't understand try again."
            if (verb == set):
                if noun == player:
                    if  number == 1:
                        pass
                    if number == 2:
                        pass
                    if number == 3:
                        pass
                    if number == 4:
                        pass
                    if number == 5:
                        pass
            
        # the text box understand six words
        elif (len(words) == 6):
            verb = words[0]
            noun = words[1]
            noun2 = words[2]
            noun3 = words[3]
            number1 = int(words[4])
            number2 = int(words[5])
            response = " I don't understand try again."
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
                            elif (number1 == 3):
                                p3.maxH = number2
                                p3.currentH = number2
                            elif (number1 == 4):
                                p4.maxH = number2
                                p4.currentH = number2
                            elif (number1 == 5):
                                p5.maxH = number2
                                p5.currentH = number2
                            
        else:
            response = " I don't understand try again."
        GW.out['text'] = "{}".format(response)

        
    def play(self):
        self.setGUI()

    def roll(self, val):
        roll = randint(1, val)
        self.RDis['text'] = [str(roll), "0" + str(roll)][roll < 10]
        
    def randRoll(self):
        die = diceVals[randint(1, 6)]
        self.roll(die)


    def changePlayerHealth(player, val):
        if (player == 1):
            Screen.PL1H['text'] = ""
    
        
#IMPORTANT DO NOT MESS WITH THIS
diceVals = [0, 4, 6, 8, 10, 12, 20]

p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
p5 = Player()
players = [p1, p2, p3, p4, p5]

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
