from sense_hat import SenseHat
from random import randint
import sys

sense = SenseHat()
sense.set_rotation(90)

# bright colors
def r():
    return randint(150,255)

# light colors
def r2():
    return randint(1,150)

def main():
    while True:
        sense.show_message("Hello! We are New Media Development :)", text_colour=[r(), r(), r()], back_colour=[r2(), r2(), r2()])
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)
