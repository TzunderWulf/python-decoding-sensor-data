import os
import glob
import csv

def load_sensor_data(sensor_data):
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    for sensor_file in sensor_files:
        with open(sensor_file=data_file):
            data_reader = csv.DictReader(data_file, delimeter=",")
            for row in data_file:
                row.append(sensor_data)
    return sensor_data
