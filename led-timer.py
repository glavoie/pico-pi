from machine import Pin, Timer
from time import sleep

led = Pin(25, Pin.OUT)

def light_led(t):
    led.value(1)

    sleep(1)

    led.value(0)

tim = Timer()
tim.init(mode=Timer.ONE_SHOT, period=2000, callback=light_led)