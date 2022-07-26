# https://forums.raspberrypi.com/viewtopic.php?t=311660
from machine import mem32, Pin
import time

LED = 25

SIO_BASE     = 0xD0000000

GPIO_OUT     = SIO_BASE + 0x010
GPIO_OUT_SET = SIO_BASE + 0x014
GPIO_OUT_CLR = SIO_BASE + 0x018
GPIO_OUT_XOR = SIO_BASE + 0x01C

Pin(25, Pin.OUT) # Initialize the PIN without using the GPIO_CTRL register

# Flash by setting all bits to a specific value
for n in range(5):
    mem32[GPIO_OUT] = 1 << LED # On  - Set bit to 1
    time.sleep(0.5)
    mem32[GPIO_OUT] = 0 << LED # Off - Set bit to 0
    time.sleep(0.5)
time.sleep(2)

# Flash by setting and clearing a specific bit
for n in range(5):
    mem32[GPIO_OUT_SET] = 1 << LED # On  - Set this bit
    time.sleep(0.25)
    mem32[GPIO_OUT_CLR] = 1 << LED # Off - Clear this bit
    time.sleep(0.25)
time.sleep(2)
   
# Flash by toggling a specific bit
for n in range(10):
    mem32[GPIO_OUT_XOR] = 1 << LED # Toggle this bit
    time.sleep(0.125)
time.sleep(2)