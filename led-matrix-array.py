# Playing with an 8x8 LED matrix connected directly to the Pico.
# Lighthing the matrix dot by dot repeatedly in a thread. 
# Source of data is a two-dimentional array. 
# Patterns coded as two-dimentional arrays.

from machine import Pin
import time
import _thread

OUT = Pin.OUT

COLS = [
    Pin(7, OUT), 
    Pin(8, OUT), 
    Pin(9, OUT), 
    Pin(10, OUT), 
    Pin(26, OUT), 
    Pin(22, OUT), 
    Pin(21, OUT), 
    Pin(20, OUT)
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

def on(row, col):
    ROWS[row].value(0)
    COLS[col].value(1)

def off(row, col):
    ROWS[row].value(1)
    COLS[col].value(0)

# Initialize empty display
DISPLAY = []
for i in range(8):
    DISPLAY.append([])
    for j in range(8):
        DISPLAY[i].append(0)

def clear():
    for i in range(8):
        for j in range(8):
            DISPLAY[i][j] = 0

def display(matrix):
    for i in range(8):
        for j in range(8):
            DISPLAY[i][j] = matrix[i][j]

STOP = False
def start_display():
    while True:
        for i in range(8):
            for j in range(8):
                if DISPLAY[i][j] == 1:
                    on(i, j)
                
                time.sleep_us(10)
                off(i, j)    
        
        if STOP:
            return

E = [
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0]
]

L = [
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0]
]

H = [
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0]
]

O = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0]
]

SMILEY = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
]

X = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1]
]

def main():
    hello = [H, E, L, L, O, SMILEY, X]

    for letter in hello:
        display(letter)
        time.sleep(0.5)
        clear()
        time.sleep(0.2)

_thread.start_new_thread(start_display, ())

main()

STOP = True
