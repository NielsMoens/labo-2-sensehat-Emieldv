from sense_hat import SenseHat
import sys
import time
from random import randint

sense = SenseHat()
sense.set_rotation(90)

def main():
    while True:
        sense.show_letter("N", [randint(0,255),randint(0,255),randint(0,255)])
        time.sleep(1)
        
        sense.show_letter("M", [randint(0,255),randint(0,255),randint(0,255)])
        time.sleep(1)
        
        sense.show_letter("D", [randint(0,255),randint(0,255),randint(0,255)])
        time.sleep(1)
        
        sense.clear()
        time.sleep(3)
    
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)