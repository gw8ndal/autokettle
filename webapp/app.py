from flask import Flask, render_template, request, redirect
from flask_sock import Sock
import os
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hce5-e9kpr8eb7J'
sock = Sock(app)

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

        if 'filesave_toggle' in data.req: # Check if the box was checked
            userdata_file = open('userdata.txt', 'w+') # Open the userdata file
            userdata_file.writelines([f'{data.raspy_pin},{data.kettle_temp}']) # Write content to the file
            userdata_file.close()
        else:
            try:
                os.remove('userdata.txt')
            except:
                pass
        return redirect('/')

@app.route('/heat', methods=['GET', 'POST'])
def heat():
    if request.method == 'GET':

        try: # Run program with data from the saved file

            userdata_file = open('userdata.txt', 'r')
            userdata_list = userdata_file.read().split(',')
            print(f'Data in the file : {userdata_list}')

            os.system(f'python ../kettle_script.py {userdata_list[0]} {userdata_list[1]}')

        except: # Run program without the data file, directly from the form
            
            print('Running without the userdata file...')

            os.system(f'python ../kettle_script.py {data.raspy_pin} {data.kettle_temp}')

        return redirect('/')
    if request.method == 'POST':
        return redirect('/')

@sock.route('/graph')
def graph(sock):
    data = 30
    while data < 100:
        data += 2
        sock.send(data)
        time.sleep(1)