from sense_hat import SenseHat
import json

sense = SenseHat()
sense.set_imu_config(False,True,False) # Gyroscope enabled

def temperature():
    data = {}
    data['unit'] = 'celsius'
    data['temp'] = sense.get_temperature()
    return json.dumps(data)

def humidity():
    data = {}
    data['unit'] = 'percentage'
    data['humidity'] = sense.get_humidity()
    return json.dumps(data)

def temperature_from_humidity():
    data = {}
    data['unit'] = 'celsius'
    data['temp_from_humidity'] = sense.get_temperature_from_humidity()
    return json.dumps(data)

def temperature_from_pressure():
    data = {}
    data['unit'] = 'celsius'
    data['temp_from_pressure'] = sense.get_temperature_from_pressure()
    return json.dumps(data)

def pressure():
    data = {}
    data['unit'] = 'milibars'
    data['pressure'] = sense.get_pressure()
    return json.dumps(data)

def orientation():
    data = {}
    data['x'] = sense.get_orientation_degrees()['pitch']
    data['y'] = sense.get_orientation_degrees()['yaw']
    data['z'] = sense.get_orientation_degrees()['roll']
    return json.dumps(data)