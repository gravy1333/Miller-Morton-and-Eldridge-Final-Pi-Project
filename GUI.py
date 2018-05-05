from Tkinter import *
from random import randint
#from Health_LED import *

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
        self.PL1L = Label(self.PLH, text='Awaiting min-max', fg='green', bg='white')
        self.PL1L.grid(row=0, column=1, sticky='news')

        self.PL2N = Label(self.PLH, text='player 2', bg='white')
        self.PL2N.grid(row=1, column=0, sticky='news')
        self.PL2L = Label(self.PLH, text='Awaiting min-max', fg='green', bg='white')
        self.PL2L.grid(row=1, column=1, sticky='news')

        self.PL3N = Label(self.PLH, text='player 3', bg='white')
        self.PL3N.grid(row=2, column=0, sticky='news')
        self.PL3L = Label(self.PLH, text='Awaiting min-max', fg='green', bg='white')
        self.PL3L.grid(row=2, column=1, sticky='news')

        self.PL4N = Label(self.PLH, text='player 4', bg='white')
        self.PL4N.grid(row=3, column=0, sticky='news')
        self.PL4L = Label(self.PLH, text='Awaiting min-max', fg='green', bg='white')
        self.PL4L.grid(row=3, column=1, sticky='news')

        self.PL5N = Label(self.PLH, text='player 5', bg='white')
        self.PL5N.grid(row=4, column=0, sticky='news')
        self.PL5L = Label(self.PLH, text='Awaiting min-max', fg='green', bg='white')
        self.PL5L.grid(row=4, column=1, sticky='news')

        for r in range(5):
            self.PLH.rowconfigure(r, weight=2)
        self.PLH.columnconfigure(0, weight=2)
        self.PLH.columnconfigure(1, weight=1)

        #player actions
        self.PLA = Label(window, text='Player actions', anchor='nw', relief='sunken')
        self.PLA.grid(row=4, column=0, rowspan=2, columnspan=4, sticky='news')

        #monster stats
        self.stats = Label(window, text='Awaiting Battle', anchor='nw', relief='sunken')
        self.stats.grid(row=0, column=4, rowspan=3, columnspan=4, sticky='news')

        #monster actions
        self.MA = Label(window, text='Moster Actions', anchor='nw', relief='sunken')
        self.MA.grid(row=4, column=4, rowspan=2, columnspan=4, sticky='news')

        #input bar
        self.player_input = Entry(window, bg='white')
        self.player_input.bind('<Return>', self.text_process())
        self.player_input.grid(row=6, column=0, columnspan=8, sticky='we')
        self.player_input.focus()
        
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
        
    def text_process(self):
        action = self.player_input.get()
        action = action.lower()
        words = action.split()
        # the text box understands three word commands
        if (len(words) == 3):
            verb = words[0]
            noun = words[1]
            number = words[2]
            response = " I don't understand try again."
            if (verb == attack):
                pass
                
            
        elif (len(words) == 4):
            verb = words[0]
            noun = words[1]
            noun2 = words[2]
            number = words[3]
            if (verb == set):
                pass
        elif (len(words) == 5):
            verb = words[0]
            noun = words[1]
            noun2 = words[2]
            number = words[3]
            number2 = words[4]
        else:
            pass

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


diceVals = [0, 4, 6, 8, 10, 12, 20]
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title('DnD Yeah boooooooooooyyyyyyyyyyy')
window.geometry('{}x{}'.format(WIDTH, HEIGHT))

GW = Screen(window)
GW.play()

window.mainloop()


    
    
