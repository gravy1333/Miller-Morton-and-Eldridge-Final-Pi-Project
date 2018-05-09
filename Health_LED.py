import time
from player import *
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

PlayersLED = [P1LED, P2LED, P3LED, P4LED, P5LED]

for element in LED:
    LED[element].start(0)

def HealthDisplay(playerNum, player):
    playerNum -= 1
    Health =  player.getHealthPercent
    
    if Health == 100:
        # 100% = green
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle(0)
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(100)
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)
    elif Health > 50:
        # transition from green to yellow
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle((100-Health)*2)
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(100-((80/50.0)*(100.0-Health)))
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)
    elif Health == 50:
        # 50% = yellow
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle(100)
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(20)
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)
    elif Health > 25:
        #transistion from yellow to red
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle(100)
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(20-((20/25.0)*(50.0-Health)))
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)
    elif Health == 25:
        # 25% = red
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle(100)
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(0)
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)
    elif Health > 0:
        # transition from red to off
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle(100-4*(25-Health))
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(0)
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)
    elif Health == 0:
        # 0% = off
        LED[PlayersLED[playerNum][0]].ChangeDutyCycle(0)
        LED[PlayersLED[playerNum][1]].ChangeDutyCycle(0)
        LED[PlayersLED[playerNum][2]].ChangeDutyCycle(0)

try:
    pass

except KeyboardInterrupt:
    for element in LED:
        LED[element].stop()
    GPIO.cleanup()
