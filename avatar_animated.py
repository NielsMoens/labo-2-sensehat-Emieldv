from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()
sense.set_rotation(90)

def main():
    while True:

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)