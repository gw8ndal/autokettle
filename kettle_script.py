import RPi.GPIO as GPIO
import time
import sys

# Use standard pinout
GPIO.setmode(GPIO.BOARD)

def heat(pin, temp):
    """
    Function used to start heating the kettle
    pin : the GPIO pin on the raspberry pi plugged to the relay
    temp : wanted temperature (Waiting for temperature sensor)
    """

    assert 0 < pin <= 40, 'Pin number must be between 1 and 40'
    
    print(f'Running on pin {pin} and target temperature {temp}°C')
    
    GPIO.setup(pin, GPIO.OUT)
    
    n = 0
    
    print('Kettle engaged')
    while n < temp:
        GPIO.setup(pin, GPIO.OUT)
        # Enable GPIO 25
        GPIO.output(pin, True)
        time.sleep(2)
        n += 1 # Simulate temperature increasing
    print('Kettle disengaged')
    GPIO.cleanup()

heat(int(sys.argv[1]), int(sys.argv[2]))
