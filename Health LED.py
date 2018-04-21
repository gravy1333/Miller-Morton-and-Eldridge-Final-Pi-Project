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

for element in LED:
    LED[element].start(0)

try:
    #100% Green 50% Yellow 0% Red
    while 1:
        Health = int(raw_input('Input Health(max 100): '))
        if Health == 100:
            LED['r1'].ChangeDutyCycle(0)
            LED['g1'].ChangeDutyCycle(100)
            LED['b1'].ChangeDutyCycle(0)
        elif Health > 50:
            LED['r1'].ChangeDutyCycle((100-Health)*2)
            LED['g1'].ChangeDutyCycle(100-((80/50)*(100-Health)))
            LED['b1'].ChangeDutyCycle(0)
        elif Health == 50:
            LED['r1'].ChangeDutyCycle(100)
            LED['g1'].ChangeDutyCycle(20)
            LED['b1'].ChangeDutyCycle(0)
        elif Health > 25:
            LED['r1'].ChangeDutyCycle(100)
            LED['g1'].ChangeDutyCycle(20-((20/25)*(50-Health)))
            LED['b1'].ChangeDutyCycle(0)
        elif Health == 25:
            LED['r1'].ChangeDutyCycle(100)
            LED['g1'].ChangeDutyCycle(0)
            LED['b1'].ChangeDutyCycle(0)
        elif Health == 0:
            LED['r1'].ChangeDutyCycle(0)
            LED['g1'].ChangeDutyCycle(0)
            LED['b1'].ChangeDutyCycle(0)
except KeyboardInterrupt:
    pass
for element in LED:
    LED[element].stop()
GPIO.cleanup()
