from django.http import HttpResponse
# from gpiozero import LED
from time import sleep

def index(request):
    return HttpResponse("Hello from index")


def status(request, pin=None):
    return HttpResponse("Status, pin={}".format(pin))


def on(request, pin):
    # LED(pin).on()
    return HttpResponse('{}'.format(pin))


def off(request, pin):
    # LED(pin).off()
    return HttpResponse('{}'.format(pin))
