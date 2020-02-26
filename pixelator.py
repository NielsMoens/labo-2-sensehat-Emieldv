from sense_hat import SenseHat
from random import randint
import time
import sys

def main():

    matrix1 = 0
    matrix2 = 0

    while matrix2 < 8 and matrix1 < 8:
        
        sense.set_pixel(matrix1, matrix2, [randint(0,255), randint(0,255), randint(0,255)])
        time.sleep(0.5)
        
        if matrix2 == 7:
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