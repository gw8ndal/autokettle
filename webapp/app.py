from flask import Flask, render_template, request, redirect
from flask_sock import Sock
import os
import time
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hce5-e9kpr8eb7J'
sock = Sock(app)
sensor = W1ThermSensor()

# Use standard pinout
GPIO.setmode(GPIO.BOARD)

@app.route('/')
def index():
    print(os.system('pwd'))
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET': # Prevent user to manually go to the data page
        return redirect('/')
    if request.method == 'POST':
        data.req = request.form # Get web form request data
        
        data.raspy_pin = data.req['GPIO_pin']
        data.kettle_temp = data.req['kettle_temp']

        userdata_file = open('userdata.txt', 'w+') # Open the userdata file
        userdata_file.writelines([f'{data.raspy_pin},{data.kettle_temp}']) # Write content to the file
        userdata_file.close()
        
        return redirect('/')

@app.route('/heat', methods=['GET', 'POST'])
def heat():
    if request.method == 'GET':

        try: # Run program with data from the saved file

            userdata_file = open('userdata.txt', 'r')
            userdata_list = userdata_file.read().split(',')
            print(f'Data in the file : {userdata_list}')
            
            while graph.sensor_temp <= int(userdata_list[1]):
                missile_launcher(int(userdata_list[0]), int(userdata_list[1]))

        except: # Run program without the data file, directly from the form
            
            print('Running without the userdata file...')

            while graph.sensor_temp <= int(userdata_list[1]):
                missile_launcher(int(data.raspy_pin), int(data.kettle_temp))

        return redirect('/')
    if request.method == 'POST':
        return redirect('/')

@sock.route('/graph')
def graph(sock):
    while True:
        graph.sensor_temp = sensor.get_temperature()
        sock.send(graph.sensor_temp)
        time.sleep(0.4)

def missile_launcher(pin, temp):
    """
    Function used to start heating the kettle
    pin : the GPIO pin on the raspberry pi plugged to the relay
    temp : wanted temperature (Waiting for temperature sensor)
    """

    # Use standard pinout
    GPIO.setmode(GPIO.BOARD)
    print(f'Running on pin {pin} and target temperature {temp}°C')
    
    GPIO.setup(pin, GPIO.OUT)
    
    n = 0
    
    print('Kettle engaged')
    print(f'current temp : {graph.sensor_temp}')
    GPIO.setup(pin, GPIO.OUT)
    # Enable GPIO 25
    GPIO.output(pin, True)
    time.sleep(2)
    n += 1 # Simulate temperature increasing
    print('Kettle disengaged')
    GPIO.cleanup()