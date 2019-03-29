#Blinky 3.0; Red, Yellow, Green Light GO!!
import RPi.GPIO as GPIO
import time

pin = 7   #Red
pin2 = 11 #Blue
pin3 = 13 #Green
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
# HIGH stands for ON.
# LOW  stands for OFF.
for i in range (0, 6):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)   
    time.sleep(0.5)

for i in range (0, 6):
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin2, GPIO.LOW)   
    time.sleep(0.5)

for i in range (0, 6):
    GPIO.output(pin3, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin3, GPIO.LOW)   
    time.sleep(0.5)
    
for i in range (0, 6):
    GPIO.output(pin3, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin, GPIO.LOW) 
    time.sleep(0.5)
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin, GPIO.HIGH) 
    time.sleep(0.7)
    GPIO.output(pin3, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin, GPIO.LOW) 
    time.sleep(0.5)
    
## Finally, clean up!
GPIO.cleanup()