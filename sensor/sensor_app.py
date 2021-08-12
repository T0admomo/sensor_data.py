# Runner script for all modules
import datetime
from particle_count_info import ParticleData
from load_data import load_sensor_data
from house_info import HouseInfo
from temperature_info import TemperatureData
from humidity_info import HumidityData
from energy_info import EnergyData
from statistics import mean
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("\nSensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print('\tLoaded records: '+ str(len(data)))

test_area = 1
test_date = datetime.datetime.strptime("5/9/20", "%m/%d/%y")

###############################################
# Module 2 code here:
house_info = HouseInfo(data)
recs = house_info.get_data_by_area('id', rec_area=test_area)
print('House sensor record for area {} = {}'.format(test_area, len(recs)))
recs = house_info.get_data_by_date('id', rec_date=test_date)
print('\tHouse sensor records for date: {} = {}'.format(test_date.strftime('%m/%d/%y'), len(recs)))

##############################################
# Module 3 code here:
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print("\nHouse Temperature sensor records for area {} = {}".format(test_area, len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))
recs = temperature_data.get_data_by_date(rec_date = test_date)
print("House Temperature sensor records for date {} = {}".format(test_date.strftime('%m/%d/%y'), len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

######################################
# Module 4 code here:
humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area = test_area)
print("\nHouse Humidity sensor records for area {} = {}".format(test_area, len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))
recs = humidity_data.get_data_by_date(rec_date = test_date)
print("House Humidity sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
print("\tAverrage: {} humidity".format(mean(recs)))

############################################
# Module 5 code here:
particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area = test_area)
print("\nHouse Particle sensor records for area {} = {}".format(test_area, len(recs)))
concentrations = particle_data.get_data_concentration(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

recs = particle_data.get_data_by_date(rec_date = test_date)
print("House Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
concentrations = particle_data.get_data_concentration(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

##################################
# Module 6 code here:
energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area = test_area)
print("\nHouse Energy sensor records for area {} = {}".format(test_area, len(recs)))
total_energy = energy_data.calculate_energy_usage(data = recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))
recs = energy_data.get_data_by_date(rec_date=test_date)
print("House Energy sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

print('\nEND OF REPORT')
