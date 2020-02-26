from sense_hat import SenseHat
import random
import sys

sense = SenseHat()
sense.set_rotation(90)
def main():
    while True:
        sense.show_message("Hello! We are New Media Development :)", text_colour=[random.randint(150,256), random.randint(150,256), random.randint(150,256)], back_colour=[random.randint(1,150), random.randint(1,150), random.randint(1,150)])
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)
