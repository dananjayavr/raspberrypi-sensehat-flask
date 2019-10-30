from flask import Flask, render_template
from sense_hat import SenseHat
from sense import temperature, humidity, temperature_from_humidity, temperature_from_pressure, pressure, orientation

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/api/v1.0/temp',methods=['GET'])
def get_temperature():
    return temperature()

@app.route('/api/v1.0/hum',methods=['GET'])
def get_humidity():
    return humidity()

@app.route('/api/v1.0/temp_hum',methods=['GET'])
def get_temp_humidity():
    return temperature_from_humidity()

@app.route('/api/v1.0/temp_pres',methods=['GET'])
def get_temp_pressure():
    return temperature_from_pressure()

@app.route('/api/v1.0/pres',methods=['GET'])
def get_pressure():
    return pressure()

@app.route('/api/v1.0/orientation',methods=['GET'])
def get_orientation():
    return orientation()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)