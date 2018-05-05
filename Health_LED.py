import time
import RPi.GPIO as GPIO
LED_Pins=[27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 13, 12, 6]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Pins, GPIO.OUT)
LED={'r1':GPIO.PWM(LED_Pins[0], 50), 'g1':GPIO.PWM(LED_Pins[1], 50), \
       'b1':GPIO.PWM(LED_Pins[2], 50), 'r2':GPIO.PWM(LED_Pins[3], 50), \
       'g2':GPIO.PWM(LED_Pins[4], 50), 'b2':GPIO.PWM(LED_Pins[5], 50), \
       'r3':GPIO.PWM(LED_Pins[6], 50), 'g3':GPIO.PWM(LED_Pins[7] , 50), \
       'b3':GPIO.PWM(LED_Pins[8], 50), 'r4':GPIO.PWM(LED_Pins[9], 50), \
       'g4':GPIO.PWM(LED_Pins[10], 50), 'b4':GPIO.PWM(LED_Pins[11], 50), \
       'r5':GPIO.PWM(LED_Pins[12], 50), 'g5':GPIO.PWM(LED_Pins[13], 50), \
       'b5':GPIO.PWM(LED_Pins[14], 50)}

P1LED = ['r1', 'g1', 'b1']
P2LED = ['r2', 'g2', 'b2']
P3LED = ['r3', 'g3', 'b3']
P4LED = ['r4', 'g4', 'b4']
P5LED = ['r5', 'g5', 'b5']

P1MaxHealth = 10.0
P2MaxHealth = 10.0
P3MaxHealth = 10.0
P4MaxHealth = 10.0
P5MaxHealth = 10.0

P1Health = 10.0
P2Health = 10.0
P3Health = 10.0
P4Health = 10.0
P5Health = 10.0

PlayersLED = [P1LED, P2LED, P3LED, P4LED, P5LED]
PlayersHealth = [P1Health, P2Health, P3Health, P4Health, P5Health]
PlayersMaxHealth = [P1MaxHealth, P2MaxHealth, P3MaxHealth, P4MaxHealth, P5MaxHealth]

for element in LED:
    LED[element].start(0)
class Player():
    def __init__(self, maxH):
        #temp is here to fix player instanciation issue
        self.tempH = maxH
        self.currentH = maxH
        self.maxH = maxH

    @property
    def maxH(self):
        return self._maxH

    @maxH.setter
    def maxH(self, val):
        if (val > 0):
            self._maxH = val

    @property
    def currentH(self):
        return self._currentH

    @currentH.setter
    def currentH(self, val):
        if (self.tempH + val < 0):
            self._currentH = 0
            self.tempH = 0

        elif (self.tempH + val >= self.maxH):
            self._currentH = self.maxH
            self.tempH = self.maxH
        else:
            self._currentH += val
            self.tempH += val

    def getHealthPercent(self):
        return int((float(self.currentH) / self.maxH) * 100)

    def __str__(self):
        return "{} / {}".format(self.currentH, self.maxH)


def HealthDisplay(playerNum, healthChange):
    player = playerNum - 1
    Health = PlayersHealth[player] + healthChange
    if (Health > PlayerMaxHealth[player]):
        Health = PlayerMaxHealth[player]
    elif (Health < 0):
        Health = 0

    HealthPercent = Health / PlayerMaxHealth[player] * 100
        
    PlayersHealth[player] = Health
    
    if HealthPercent == 100:
        # 100% = green
        LED[PlayersLED[player][0]].ChangeDutyCycle(0)
        LED[PlayersLED[player][1]].ChangeDutyCycle(100)
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)
    elif HealthPercent > 50:
        # transition from green to yellow
        LED[PlayersLED[player][0]].ChangeDutyCycle((100-Health)*2)
        LED[PlayersLED[player][1]].ChangeDutyCycle(100-((80/50.0)*(100.0-Health)))
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)
    elif HealthPercent == 50:
        # 50% = yellow
        LED[PlayersLED[player][0]].ChangeDutyCycle(100)
        LED[PlayersLED[player][1]].ChangeDutyCycle(20)
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)
    elif HealthPercent > 25:
        #transistion from yellow to red
        LED[PlayersLED[player][0]].ChangeDutyCycle(100)
        LED[PlayersLED[player][1]].ChangeDutyCycle(20-((20/25.0)*(50.0-Health)))
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)
    elif HealthPercent == 25:
        # 25% = red
        LED[PlayersLED[player][0]].ChangeDutyCycle(100)
        LED[PlayersLED[player][1]].ChangeDutyCycle(0)
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)
    elif HealthPercent > 0:
        # transition from red to off
        LED[PlayersLED[player][0]].ChangeDutyCycle(100-4*(25-Health))
        LED[PlayersLED[player][1]].ChangeDutyCycle(0)
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)
    elif HealthPercent == 0:
        # 0% = off
        LED[PlayersLED[player][0]].ChangeDutyCycle(0)
        LED[PlayersLED[player][1]].ChangeDutyCycle(0)
        LED[PlayersLED[player][2]].ChangeDutyCycle(0)

    

try:
    # 100% Green 50% Yellow 0% Red
    while True:
        action = raw_input('Input player number and amount to change haelth(ie 1 -25): ')
        words = action.split()
        HealthDisplay(int(words[0]), float(words[1]))

except KeyboardInterrupt:
    for element in LED:
        LED[element].stop()
    GPIO.cleanup()
