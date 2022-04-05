import RPi.GPIO as GPIO
import time
import sys

# Use standard pinout
GPIO.setmode(GPIO.BOARD)

def testing(pin, temp):
    """
    Function used to test the output of a GPIO pin
    pin : the GPIO pin on the raspberry pi
    temp : wanted temperature (TBD)
    """
    assert 0 < pin <= 40
    
    GPIO.setup(pin, GPIO.OUT)
    n = 0
    while n < temp:
        GPIO.setup(pin, GPIO.OUT)
        print(temp)
        # Enable GPIO 25
        GPIO.output(pin, True)
        print('on')
        time.sleep(1)
        n += 1
    GPIO.cleanup()
print(int(sys.argv[1]), int(sys.argv[2]))
# testing(int(sys.argv[1]), int(sys.argv[2]))
