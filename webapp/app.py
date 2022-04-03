from crypt import methods
from flask import Flask, render_template, request, redirect, flash
import paramiko # Module to connect to SSH in python
from scp import SCPClient # Module to upload files via SSH
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET': # Prevent user to manually go to the data page
        return redirect('/')
    if request.method == 'POST':
        data.req = request.form # Get web form request data

        data.raspy_pin = data.req['GPIO_pin']
        data.raspy_ip = data.req['raspy_ip']
        data.raspy_user = data.req['raspy_user']
        data.raspy_pass = data.req['raspy_pass']

        if 'filesave_toggle' in data.req: # Check if the box was checked
            userdata_file = open('userdata.txt', 'w+') # Open the userdata file
            userdata_file.writelines([f'{data.raspy_pin}\n', f'{data.raspy_ip}\n', f'{data.raspy_user}\n', f'{data.raspy_pass}\n']) # Write content to the file
            userdata_file.close()
        else:
            os.remove('userdata.txt')
        return redirect('/')

@app.route('/heat', methods=['GET', 'POST'])
def heat():
    if request.method == 'GET':

        try: # Run program with data from the saved file

            userdata_file = open('userdata.txt', 'r')
            userdata_list = userdata_file.read().split('\n')
            print(userdata_list)
            print('avec fichier')
            ssh_connection = paramiko.SSHClient()
            ssh_connection.load_system_host_keys()
            ssh_connection.connect(userdata_list[1], username=userdata_list[2], password=userdata_list[3]) # Connect to the raspberry pi
            
            with SCPClient(ssh_connection.get_transport()) as scp: # Copy requirements file and the python script to the raspberry pi
                scp.put('../kettle_script.py', '/tmp')
                scp.put('kettle_reqs.txt', '/tmp')
            
            stdin, stdout, stderr = ssh_connection.exec_command(f'cd /tmp ; python3 -m pip install -r kettle_reqs.txt ; python3 kettle_script.py {userdata_list[0]}') # Install requirements and execute the script with the selected pin
            print(stdout)

        except: # Run program without the data file, directly from the form
            print('sans fichier')
            ssh_connection = paramiko.SSHClient()
            ssh_connection.load_system_host_keys()
            ssh_connection.connect(data.raspy_ip, username=data.raspy_user, password=data.raspy_pass) # Connect to the raspberry pi
            
            with SCPClient(ssh_connection.get_transport()) as scp:   
                scp.put('../kettle_script.py', '/tmp')
                scp.put('kettle_reqs.txt', '/tmp')
            
            stdin, stdout, stderr = ssh_connection.exec_command(f'cd /tmp ; python3 -m pip install -r kettle_reqs.txt ; python3 kettle_script.py {data.raspy_pin}') # Install requirements and execute the script with the selected pin
            print(stdout)

        return redirect('/')
    if request.method == 'POST':
        return redirect('/')