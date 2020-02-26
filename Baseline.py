from sense_hat import SenseHat
from random import randint
import sys

sense = SenseHat()
sense.set_rotation(90)
def main():
    while True:
        sense.show_message("Hello! We are New Media Development :)", text_colour=[randint(150,256), randint(150,256), randint(150,256)], back_colour=[randint(1,150), randint(1,150), randint(1,150)])
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)
