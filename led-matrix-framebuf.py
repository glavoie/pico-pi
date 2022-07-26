# Playing with an 8x8 LED matrix connected directly to the Pico.
# Lighthing the matrix dot by dot repeatedly in a thread, using the Pin API.
# Source of data is a framebuf which allows more advanced manipulations and supports displaying text

from machine import Pin
import time
import _thread
import framebuf

OUT = Pin.OUT

COLS = [
    Pin(7, OUT, value = 0), 
    Pin(8, OUT, value = 0), 
    Pin(9, OUT, value = 0), 
    Pin(10, OUT, value = 0), 
    Pin(26, OUT, value = 0), 
    Pin(22, OUT, value = 0), 
    Pin(21, OUT, value = 0), 
    Pin(20, OUT, value = 0)
]
ROWS = [
    Pin(19, OUT, value = 1), 
    Pin(18, OUT, value = 1), 
    Pin(17, OUT, value = 1), 
    Pin(16, OUT, value = 1), 
    Pin(11, OUT, value = 1), 
    Pin(12, OUT, value = 1), 
    Pin(13, OUT, value = 1), 
    Pin(14, OUT, value = 1)
]

BUF = bytearray(256) 
fbuf = framebuf.FrameBuffer(BUF, 256, 8, framebuf.MONO_VLSB)

HEART = framebuf.FrameBuffer(bytearray(b'\x0c\x1e\x3e\x7c\x7c\x3e\x1e\x0c'), 8, 8, framebuf.MONO_VLSB)

STOP = False
def start_display():
    while True:
        for i in range(8):
            COLS[i].value(1)
            for j in range(8):
                ROWS[j].value(~BUF[i] >> j & 1)
                time.sleep_us(10)
                ROWS[j].value(1)

            COLS[i].value(0)
        
        if STOP:
            return

def main():
    TEXT="Hello!"
    fbuf.text(TEXT, 16, 0)
    fbuf.blit(HEART, 8, 0)
    fbuf.blit(HEART, (len(TEXT) + 2) * 8, 0)

    for i in range((len(TEXT) + 4) * 8):
        fbuf.scroll(-1, 0)
        time.sleep_ms(100)

_thread.start_new_thread(start_display, ())
main()

STOP = True
