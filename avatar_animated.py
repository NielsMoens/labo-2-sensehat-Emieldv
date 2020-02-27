from sense_hat import SenseHat
from time import sleep
from PIL import Image
from random import randint
import sys

sense = SenseHat()
sense.set_rotation(90)

img1 = Image.open("img/avatar1.jpg")
img1_pixels = list(img1.getdata())
img2 = Image.open("img/avatar2.jpg")
img2_pixels = list(img2.getdata())
img3 = Image.open("img/avatar3.jpg")
img3_pixels = list(img3.getdata())
img4 = Image.open("img/avatar4.jpg")
img4_pixels = list(img4.getdata())
img5 = Image.open("img/avatar5.jpg")
img5_pixels = list(img5.getdata())
img6 = Image.open("img/avatar6.jpg")
img6_pixels = list(img6.getdata())
img7 = Image.open("img/avatar7.jpg")
img7_pixels = list(img7.getdata())

def main():
    while True:
        sense.set_pixels(img1_pixels)
        random = randint(1,7)
        if random == 1:
            sense.set_pixels(img1_pixels)
            sleep(2)
        elif random == 2:
            sense.set_pixels(img2_pixels)
            sleep(2)
        elif random == 3:
            sense.set_pixels(img3_pixels)
            sleep(2)
        elif random == 4:
            sense.set_pixels(img4_pixels)
            sleep(2)
        elif random == 5:
            sense.set_pixels(img5_pixels)
            sleep(2)
        elif random == 6:
            sense.set_pixels(img6_pixels)
            sleep(2)
        elif random == 7:
            sense.set_pixels(img7_pixels)
            sleep(2)
        

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)