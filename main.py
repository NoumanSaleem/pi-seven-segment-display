import time
from functools import partial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

segmentPins = { 'a': 17, 'b': 22, 'c': 8, 'd': 25, 'e': 24, 'f': 27, 'g': 7 }
pinSlots = { 'a': 0b00000001, 'b': 0b00000010, 'c': 0b00000100, 'd': 0b00001000, 'e': 0b00010000, 'f': 0b00100000, 'g': 0b01000000 }
valMap = { 0: 0b00111111, 1: 0b00000110, 2: 0b01011011, 3: 0b01001111, 4: 0b01100110, 5: 0b01101101, 6: 0b01111101, 7: 0b00000111, 8: 0b01111111, 9: 0b01100111 }

def renderChar(c):
    val = valMap[c]

    GPIO.output(list(segmentPins.values()), GPIO.LOW)

    for k,v in pinSlots.items():
        if val&v == v:
            GPIO.output(segmentPins[k], GPIO.HIGH)

try:
    GPIO.setup(list(segmentPins.values()), GPIO.OUT)
    GPIO.output(list(segmentPins.values()), GPIO.LOW)

    val = 0

    while True:
        renderChar(val)
        val = 0 if val == 9 else (val + 1)
        time.sleep(1)
except KeyboardInterrupt:
        print("Goodbye")
finally:
        GPIO.cleanup()

