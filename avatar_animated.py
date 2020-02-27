from sense_hat import SenseHat
from time import sleep
from PIL import Image
import sys

sense = SenseHat()
sense.set_rotation(90)

# image1 = Image.open("img/avatar1.jpg")
# image2 = Image.open("img/avatar2.jpg")

sense.set_pixels("img/avatar6.jpg")

# def main():
#     while True:
#         sense.set_pixels(image2)
#         sleep(2)

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)