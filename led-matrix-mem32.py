# Playing with an 8x8 LED matrix connected directly to the Pico.
# Lighthing the matrix dot by dot repeatedly in a thread, updating all pins at once through the GPIO_OUT register.
# This method allows for a faster refresh and a brighter display.
# Source of data is a framebuf which allows more advanced manipulations and supports displaying text

from machine import Pin, mem32
import time
import _thread
import framebuf

SIO_BASE     = 0xD0000000
GPIO_OUT     = SIO_BASE + 0x0010
GPIO_OUT_SET = SIO_BASE + 0x0014
GPIO_OUT_CLR = SIO_BASE + 0x0018
GPIO_OUT_XOR = SIO_BASE + 0x001C

COLS = [
    7, 
    8, 
    9, 
    10, 
    26, 
    22, 
    21, 
    20, 
]

ROWS = [
    19, 
    18,  
    17,  
    16, 
    11, 
    12, 
    13, 
    14,
]

ROWS_MASK = 0
for col in COLS:
    Pin(col, Pin.OUT) # Setting the PIN in SIO (GPIO) mode
for row in ROWS:
    Pin(row, Pin.OUT) # Setting the PIN in SIO (GPIO) mode
    ROWS_MASK |= 1 << row

BUF = bytearray(256) 
fbuf = framebuf.FrameBuffer(BUF, 256, 8, framebuf.MONO_VLSB)

HEART = framebuf.FrameBuffer(bytearray(b'\x0c\x1e\x3e\x7c\x7c\x3e\x1e\x0c'), 8, 8, framebuf.MONO_VLSB)

STOP = False
def start_display():
    while True:
        for i in range(8):
            for j in range(8):
                mem32[GPIO_OUT] = 1 << COLS[i] | (BUF[i] >> j & 1) << ROWS[j] ^ ROWS_MASK
                time.sleep_us(10)
        
        if STOP:
            return

def main(): 
    TEXT="Hello!"
    fbuf.blit(HEART, 8, 0)
    fbuf.text(TEXT, 16, 0)
    fbuf.blit(HEART, (len(TEXT) + 2) * 8, 0)

    for i in range((len(TEXT) + 4) * 8):
        fbuf.scroll(-1, 0)
        time.sleep_ms(100)

_thread.start_new_thread(start_display, ())

main()


STOP = True
