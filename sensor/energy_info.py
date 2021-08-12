from house_info import HouseInfo
import datetime

class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = int('0x0F0', base=16)

    def __init__(self, data):
        self.data = data

    def _get_energy(self, rec_energy):
        # produce an integer from the hexidecimal code
        energy: int = int(rec_energy, base=16)
        energy = (energy & self.ENERGY_BITS) >> 4
        return energy

    def _convert_data(self, data):
        field_data = []
        for record in data:
            field_data.append(self._get_energy(record))
        return field_data

    def get_data_by_area(self, rec_area=0):
        field_data = super().get_data_by_area('energy_usage', rec_area)
        return self._convert_data(field_data)

    def get_data_by_date(self, rec_date=datetime.date.today()):
        field_data = super().get_data_by_date('energy_usage', rec_date)
        return self._convert_data(field_data)

    # The purpose of this method is to take a list of energy usage values
    # , calculate  the cost per light bulb usage,
    # and return the sum of all the values in the data list.
    def calculate_energy_usage(self, data):
        total_energy = sum(field * self.ENERGY_PER_BULB for field in data)
        return total_energy


