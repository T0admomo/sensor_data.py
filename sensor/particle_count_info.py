from house_info import HouseInfo
import datetime

class ParticleData(HouseInfo):

    def __init__(self, data):
        self.data = data

    def _convert_data(self, data):
        field_data = []
        for record in data:
            field_data.append(float(record))
        return field_data

    def get_data_by_area(self,  rec_area=0):
        field_data = super().get_data_by_area('particulate', rec_area)
        return self._convert_data(field_data)

    def get_data_by_date(self, rec_date=datetime.date.today()):
        field_data = super().get_data_by_date('particulate', rec_date)
        return self._convert_data(field_data)

    def get_data_concentration(self, data):
        particulate_dict = {"good": 0,
                            "moderate": 0,
                            "bad": 0}
        for record in data:
            if record < 50.0:
                particulate_dict['good'] += 1
            elif record < 100:
                particulate_dict['moderate'] += 1
            else:
                particulate_dict['bad'] += 1

        return particulate_dict

