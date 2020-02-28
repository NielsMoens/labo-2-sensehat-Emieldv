from sense_hat import SenseHat
from random import randint
import time
import sys

sense = SenseHat()

def r():
    return randint(1,255)

def main():

    matrix1 = 0
    matrix2 = 0

    while True:
        
        sense.set_pixel(matrix1, matrix2, [r(), r(), r()])
        time.sleep(0.2)
        sense.clear()
        
        if matrix2 == 7 and matrix1 == 7:
            matrix1 = 0
            matrix2 = 0
        elif matrix2 == 7:
            matrix2 = 0
            matrix1 += 1
        else:
            matrix2 +=1
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)