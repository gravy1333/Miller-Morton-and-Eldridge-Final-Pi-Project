from Tkinter import *
import dice_rolls as DRs

class Screen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

    def setGUI(self):
        diceVals = [None, 4, 6, 8, 10, 12, 20]
        #upper part
        Screen.PLH = Label(self, text="PLayer Health").grid(row=0, column=0, rowspan=3, columnspan=3)
        Screen.stats = Label(self, text="Stats").grid(row=0, column=4, rowspan=3, columnspan=3)
        Screen.MA = Label(self, text="Moster Actions").grid(row=4, column=0, rowspan=2, columnspan=3)
        Screen.PLA = Label(self, text="Player actions").grid(row=4, column=4, rowspan=2, columnspan=3)
        Screen.player_input = Entry(self, bg='white').grid(row=6, column=0, columnspan=7)
        Screen.player_input.bind("<Return>", self.text_process())
        
        #dice buttons
        Screen.d4 = Button(self, bg='white', text="d4", width=1)
        Screen.d4.grid(row=7, column=0)
    
        Screen.d6 = Button(self, bg='white', text="d6", width=1)
        Screen.d6.grid(row=7, column=1)
        
        Screen.d8 = Button(self, bg='white', text="d8", width=1)
        Screen.d8.grid(row=7, column=2)
        
        Screen.d10 = Button(self, bg='white', text="d10", width=1)
        Screen.d10.grid(row=7, column=3)
        
        Screen.d12 = Button(self, bg='white', text="d12", width=1)
        Screen.d12.grid(row=7, column=4)
        
        Screen.d20 = Button(self, bg='white', text="d20", width=1)
        Screen.d20.grid(row=7, column=5)

        Screen.dRand = Button(self, bg='white', text="Random\nDice", width=1)
        Screen.dRand.grid(row=7, column=6)
        
        Screen.DR = Lable(self, bg='white', text='0').grid(row=7, column=7)
        for b in range(1, 7):
            Screen.bind('<{}>'.format(b), DRs._{}sided_dice_roll().format(diceVals[b])

        Screen.bind('<7>', self.randRoll)
        
    def play(self):
        self.setGUI()
        #
    
    def randRoll(self):
        die = DRs.randomDie()
        return DRs._{}sided_dice_roll().format(diceVals[die])

    
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("DnD Yeah boooooooooooyyyyyyyyyyy")

GW = Screen(window)
GW.play()
window.mainloop()
