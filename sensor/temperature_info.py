from house_info import HouseInfo
import datetime

class TemperatureData(HouseInfo):

    def __init__(self, data):
        self.data = data

    def _convert_data(self, data):
        field_data = []
        for record in data:
            field_data.append(int(str(record), base=10))
        return field_data

    def get_data_by_area(self, rec_area=0):
        field_data = super().get_data_by_area("temperature", rec_area)
        return self._convert_data(field_data)

    def get_data_by_date(self, rec_date=datetime.date.today()):
        field_data = super().get_data_by_date("temperature", rec_date)
        return self._convert_data(field_data)
