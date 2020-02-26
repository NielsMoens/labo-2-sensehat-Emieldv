from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()
sense.set_rotation(90)


r = (255, 0, 0)
b = (0, 0, 255)
h = (252, 160, 72)
e = (0, 0, 0)

image = [
e,e,e,e,r,r,e,e,
e,e,e,r,r,r,r,r,
e,e,e,h,e,h,e,e,
e,e,e,h,h,h,h,e,
e,e,b,b,r,b,r,e,
e,b,e,b,h,r,h,b,
e,e,e,r,r,r,r,e,
e,e,e,r,e,e,r,e
]

image2 = [
e,e,e,h,e,h,e,e,
e,e,e,h,h,h,h,e,
e,e,b,b,r,b,r,e,
e,b,e,b,h,r,h,b,
e,e,e,r,r,r,r,e,
e,e,e,r,e,e,r,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

sense.set_pixels(image)

def main():
    while True:
        sleep(1)
        sense.flip_h()
        
        for event in sense.stick.get_events():
            sense.set_pixels(image2)
            sense.flip_h()
            sleep(0.2)
            sense.set_pixels(image)
            
    
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)