import RPi.GPIO as GPIO

def turnOn(state):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,state)
    