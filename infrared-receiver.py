from machine import Timer, Pin, PWM
import utime
from time import sleep

stream = []
started = False
timer = Timer(-1)

def timer_callback(timer):
    global stream
    global started

    # Dump the captured edges
    print("-----CAPTURE-----")
    for i in range(len(stream)):
        diff = 0
        if i > 0:
            diff = utime.ticks_diff(stream[i][1], stream[i - 1][1])

        # Edge number, Value, Duration
        print(str(i) + ", " + str(stream[i][0]) + ", " + str(diff))

    print("-----END OF CAPTURE-----")
    started = False
    stream = []

def callback(pin):
    global stream
    global started
    global timer 
    
    if started == False:
        # Capture for 500ms
        timer.init(period=500, mode=Timer.ONE_SHOT, callback=timer_callback)
        started = True

    stream.append((pin.value(), utime.ticks_us()))
    
pin = Pin(22, Pin.IN)
pin.irq(callback, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)

while True:
    sleep(1)