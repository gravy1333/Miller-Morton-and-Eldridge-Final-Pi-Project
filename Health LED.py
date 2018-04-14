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
LED['r1'].start(0)
LED['b1'].start(0)
try:
    #100% Green 50% Yellow 0% Red
    while 1:
        for dc in range(0, 101, 5):
            LED['r1'].ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            LED['r1'].ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(0, 101, 5):
            LED['b1'].ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            LED['b1'].ChangeDutyCycle(dc)
            time.sleep(0.1)
                
except KeyboardInterrupt:
    pass
LED['r1'].stop()
LED['b1'].stop()
GPIO.cleanup()
