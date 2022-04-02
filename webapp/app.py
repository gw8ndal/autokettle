from crypt import methods
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        req = request.form

        data.raspy_pin = req['GPIO_pin']
        data.raspy_ip = req['raspy_ip']
        data.raspy_user = req['raspy_user']
        data.raspy_pass = req['raspy_pass']

        print(data.raspy_pin, data.raspy_ip, data.raspy_user, data.raspy_pass)
        return redirect('/')

@app.route('/heat', methods=['GET', 'POST'])
def heat():
    if request.method == 'GET':
        return redirect('/data')
    if request.method == 'POST':
        print(f'ça chauffe sur le pin {data.raspy_pin}')
        return render_template('index.html')
