import pandas as pd

class ExcelExporter:
    def __init__(self, relocation_list):
        uid = "Bike"
        station1 = "previous station"
        station2 = "new station"
        name = "name"
        bike_list = []
        user_list = []
        station1_list = []
        station2_list = []

        for relocation in relocation_list:
            rel_data = relocation.get_data()
            bike_list.append(rel_data[0])
            user_list.append(rel_data[1])
            station1_list.append(rel_data[2])
            station2_list.append(rel_data[3])

        data = pd.DataFrame({uid:bike_list, station1:station1_list, station2:station2_list, name:user_list})
        data.to_excel('relocations.xlsx', sheet_name='relocations', index=False)
