import machine
from ws2812 import WS2812
import utime
import urandom

ws = WS2812(machine.Pin(0),8)

def light_out():
    for j in range(8):
        ws[j] = [0,0,0]

    ws.write()
    utime.sleep_ms(100)

def light(position, color):
    light_out()
    ws[position] = color
    ws.write()  
    utime.sleep_ms(100)

while True:
    print("green")
    light(1, [0, 50, 25])
    utime.sleep_ms(8000)

    print("yellow")
    light(2, [50, 10, 0])
    utime.sleep_ms(2000)

    print("red")
    light(3, [50, 0, 0])
    utime.sleep_ms(8000)
    
    