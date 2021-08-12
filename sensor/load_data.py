import os
import glob
import csv

def load_sensor_data():
    sensor_data = []
    # all files in directory
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv')) # remove ../ when running from top level CL
    for sensor_file in sensor_files:
        with open(sensor_file, 'r') as data_file:
            # read each file
            data_reader = csv.DictReader(data_file, delimiter=",")
            # add to output
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data