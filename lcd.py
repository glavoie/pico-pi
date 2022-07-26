from lcd1602 import LCD
import utime

lcd = LCD()
lcd.clear()
string = " Hello!\n"
lcd.message(string)
utime.sleep(2)
lcd.write(2, 1, "World!")
utime.sleep(2)
