from sense_hat import SenseHat
from random import randint
import sys
import time

sense = SenseHat()
sense.set_rotation(90)

# ask for a string and make an array 
string = input("Geef een woord in:\n")
string_array = [str(x) for x in str(string)]

# calculate array length
string_length = len(string_array)

speed = input("Geef de snelheid in seconden in:\n")

def r():
    return randint(1,255)

def main():

    string_location = 0

    while True:
        
        if string_location < string_length:
            sense.show_letter(string_array[string_location], [r(),r(),r()])
            string_location += 1
            time.sleep(float(speed))
        else:
            string_location = 0
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