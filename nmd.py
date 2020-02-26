from sense_hat import SenseHat
import sys
import time
import random

sense = SenseHat()
sense.set_rotation(90)

def main():
    while True:
        sense.show_letter("N", [random.randint(1,256),random.randint(1,256),random.randint(1,256)])
        time.sleep(1)
        
        sense.show_letter("M", [random.randint(1,256),random.randint(1,256),random.randint(1,256)])
        time.sleep(1)
        
        sense.show_letter("D", [random.randint(1,256),random.randint(1,256),random.randint(1,256)])
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