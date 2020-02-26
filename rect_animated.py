from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()

r = (255, 0, 0)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]
image2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,r,r,r,r,e,e,
e,e,r,e,e,r,e,e,
e,e,r,e,e,r,e,e,
e,e,r,r,r,r,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]
image3 = [
e,e,e,e,e,e,e,e,
e,r,r,r,r,r,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,r,r,r,r,r,r,e,
e,e,e,e,e,e,e,e,
]
image4 = [
r,r,r,r,r,r,r,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,e,e,e,e,e,e,r,
r,r,r,r,r,r,r,r,
]

def main():
    while True:
        sense.set_pixels(image)
        sleep,(0.5)
        sense.set_pixels(image2)
        sleep(0.5)
        sense.set_pixels(image3)
        sleep(0.5)
        sense.set_pixels(image4)
        sleep(0.5)
        sense.set_pixels(image3)
        sleep(0.5)
        sense.set_pixels(image2)
        sleep(0.5)

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)