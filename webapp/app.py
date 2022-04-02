from crypt import methods
from flask import Flask, render_template, request, redirect, flash
import paramiko # Module to connect to SSH in python
from scp import SCPClient # Module to upload files via SSH

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET': # Prevent user to manually go to the data page
        return redirect('/')
    if request.method == 'POST':
        req = request.form # Get web form request data

        data.raspy_pin = req['GPIO_pin']
        data.raspy_ip = req['raspy_ip']
        data.raspy_user = req['raspy_user']
        data.raspy_pass = req['raspy_pass']

        if 'filesave_toggle' in req: # Check if the box was checked
            userdata_file = open('userdata.txt', 'w+') # Open the userdata file
            userdata_file.writelines([f'{data.raspy_pin}\n', f'{data.raspy_ip}\n', f'{data.raspy_user}\n', f'{data.raspy_pass}\n']) # Write content to the file
            userdata_file.close()
        return redirect('/')

@app.route('/heat', methods=['GET', 'POST'])
def heat():
    if request.method == 'GET':

        userdata_file = open('userdata.txt', 'r')
        userdata_list = userdata_file.read().split('\n')
        print(userdata_list)

        ssh_connection = paramiko.SSHClient()
        ssh_connection.load_system_host_keys()
        ssh_connection.connect(data.raspy_ip, username=data.raspy_user, password=data.raspy_pass) # Connect to the raspberry pi
        
        with SCPClient(ssh_connection.get_transport()) as scp:   
            scp.put('../kettle_script.py', '/tmp')
            scp.put('kettle_reqs.txt', '/tmp')
        
        stdin, stdout, stderr = ssh_connection.exec_command('cd /tmp ; python3 -m pip install -r kettle_reqs.txt ; python3 kettle_script.py') # Install requirements and execute the script

        return redirect('/')
    if request.method == 'POST':
        return redirect('/')