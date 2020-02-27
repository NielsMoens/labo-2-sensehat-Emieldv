from sense_hat import SenseHat
from random import randint
import sys
import time

sense = SenseHat()
sense.set_rotation(90)

def main():
    while True:
        sense.show_letter("N", [randint(1,256),randint(1,256),randint(1,256)])
        time.sleep(1)
        
        sense.show_letter("M", [randint(1,256),randint(1,256),randint(1,256)])
        time.sleep(1)
        
        sense.show_letter("D", [randint(1,256),randint(1,256),randint(1,256)])
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