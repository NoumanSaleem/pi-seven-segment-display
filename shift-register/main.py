import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

valMap = { 0: 0b00111111, 1: 0b00000110, 2: 0b01011011, 3: 0b01001111, 4: 0b01100110, 5: 0b01101101, 6: 0b01111101, 7: 0b00000111, 8: 0b01111111, 9: 0b01100111 }

PIN_DATA  = 17
PIN_LATCH = 27
PIN_CLOCK = 22
GPIO.setup(PIN_DATA,  GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def shiftout(byte):
    GPIO.output(PIN_LATCH, 0)
    for x in range(8):
        GPIO.output(PIN_DATA, (byte >> x) & 1)
        GPIO.output(PIN_CLOCK, 1)
        GPIO.output(PIN_CLOCK, 0)
    GPIO.output(PIN_LATCH, 1)

try:
    val = 0
    while True:
        shiftout(valMap[val])
        val = 0 if val == 9 else (val + 1)
        time.sleep(1)
except KeyboardInterrupt:
        print("Goodbye")
finally:
        GPIO.cleanup()

