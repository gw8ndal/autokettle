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
    while True:
        GPIO.setup(pin, GPIO.OUT)
        
        # Enable GPIO 25
        GPIO.output(pin, True)
        print('on')
        
        time.sleep(10)
        
        # Disable GPIO 25
        GPIO.output(pin, False)
        print('off')
        
        GPIO.cleanup()

testing(int(sys.argv[1]), int(sys.argv[2]))
