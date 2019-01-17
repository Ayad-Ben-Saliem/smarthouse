from django.http import HttpResponse
# from gpiozero import LED
from time import sleep
import os
import RPi.GPIO as GPIO

LAMP1_PIN = 11
LAMP2_PIN = 12
GATE_PIN  = 13

LAMP1_PIN_STATUS = 'off'
LAMP2_PIN_STATUS = 'off'
GATE_PIN_STATUS = 'off'

GPIO.setmode(GPIO.BOARD)
pins = [LAMP1_PIN, LAMP2_PIN, GATE_PIN]
GPIO.setup(pins, GPIO.OUT)

PWM = GPIO.PWM(GATE_PIN, 50) # Pin 13 for PWM with 50Hz

def get_status(pin):
    if   pin is LAMP1_PIN:
        return LAMP1_PIN_STATUS
    elif pin is LAMP2_PIN:
        return LAMP2_PIN_STATUS
    elif pi is GATE_PIN:
        return GATE_PIN_STATUS

def set_status(pin, status):
    if   pin is LAMP1_PIN:
        global LAMP1_PIN_STATUS
        LAMP1_PIN_STATUS = status
    elif pin is LAMP2_PIN:
        global LAMP2_PIN_STATUS
        LAMP2_PIN_STATUS = status
    elif pin is LAMP2_PIN:
        global GATE_PIN_STATUS
        GATE_PIN_STATUS = status

def index(request):
    return HttpResponse("Hello from index")

def check_pin(pin):
    return pin is not LAMP1_PIN and pin is not LAMP2_PIN and pin is not GATE_PIN and pin is not None

def status(request, pin=None):
    if check_pin(pin):
        return HttpResponse("Wrong pin".format(pin))
    if pin is None:
        descreption = 'pin {} is {} '.format(LAMP1_PIN, LAMP1_PIN_STATUS)
        descreption+= ',and {} is {}'.format(LAMP2_PIN, LAMP2_PIN_STATUS)
        descreption+= ',and {} is {}'.format(GATE_PIN , GATE_PIN_STATUS)
    else:
        descreption = 'pin {} is {}'.format(pin, get_status(pin))
    os.system('espeak "{}"'.format(descreption))
    return HttpResponse("Status, " + descreption)


def on(request, pin):
    if check_pin(pin):
        return HttpResponse("Wrong pin".format(pin))
    os.system('espeak "make pin {} on"'.format(pin))
    if pin is LAMP1_PIN or pin is LAMP2_PIN:
        GPIO.output(pin, GPIO.HIGH)
    elif pin is GATE_PIN:
        PWM.start(50) # Initialization
        for i in range(50, 76):
            PWM.ChangeDutyCycle(i)
            print(i)
            sleep(0.01)
        PWM.stop()
    set_status(pin, 'on')
    return HttpResponse('{}'.format(pin))


def off(request, pin):
    # LED(pin).off()
    os.system('espeak "make pin {} off"'.format(pin))
    if pin is LAMP1_PIN or pin is LAMP2_PIN:
        GPIO.output(pin, GPIO.LOW)
    elif pin is GATE_PIN:
        PWM.start(75) # Initialization
        for i in range(75, 49, -1):
            PWM.ChangeDutyCycle(i)
            print(i)
            sleep(0.01)
        PWM.stop()
    set_status(pin, 'off')
    return HttpResponse('{}'.format(pin))
