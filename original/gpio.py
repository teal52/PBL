import RPi.GPIO as gp


def switch(state):
    gp.setmode(gp.BOARD)
    gp.setup(11,gp.OUT)
    gp.output(11,state)