from machine import Pin
import time

led = Pin(25, Pin.OUT)

led.value(1)

time.sleep(1)

led.value(0)