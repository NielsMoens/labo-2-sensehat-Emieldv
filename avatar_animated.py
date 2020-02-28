from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

sense = SenseHat()

dimention = int(input("Hoe groot moet de avatar zijn?\n8x8 -> type 8\n6x6 -> type 6\n4x4 -> type 4\n\n"))

rood = int(input("\nGeef het aantal rood in (1-255)\n"))
groen = int(input("Geef het aantal groen in (1-255)\n"))
blauw = int(input("Geef het aantal blauw in (1-255)\n"))

e = (0, 0, 0)
c = (rood, groen, blauw)

speed = float(input("\nGeef de snelheid in seconden:\n"))

def color():
    return randint(1,255)

def main():

    def r():
        pixel = randint(1,2)

        if pixel == 1:
            return e
        else:
            return c

    while True:

        if dimention == 6:
            imagehalf_6wide = [
            e,e,e,e,e,e,e,e,
            e,r(),r(),r(),r(),r(),r(),e,
            e,r(),r(),r(),r(),r(),r(),e,
            e,r(),r(),r(),r(),r(),r(),e,
            ]
            fullimage = imagehalf_6wide + imagehalf_6wide[::-1]
        elif dimention == 4:
            imagehalf_4wide = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,r(),r(),r(),r(),e,e,
            e,e,r(),r(),r(),r(),e,e,
            ]
            fullimage = imagehalf_4wide + imagehalf_4wide[::-1]
        else:
            imagehalf_8wide = [
            r(),r(),r(),r(),r(),r(),r(),r(),
            r(),r(),r(),r(),r(),r(),r(),r(),
            r(),r(),r(),r(),r(),r(),r(),r(),
            r(),r(),r(),r(),r(),r(),r(),r(),
            ]
            fullimage = imagehalf_8wide + imagehalf_8wide[::-1]

        sense.set_pixels(fullimage)
        sleep(speed)
        sense.clear()

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)