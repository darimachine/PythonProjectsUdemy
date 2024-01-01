#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
sheety = DataManager()
sheety.user_information()
sheet_data = sheety.data["prices"]

is_empty_space = False
pprint(sheet_data)
for data in sheet_data:
    if data["iataCode"]=="":
        flight_sear = FlightSearch()
        data["iataCode"]=  flight_sear.update(data["city"])
        is_empty_space=True
if is_empty_space:
    sheety.update_sheet(sheet_data)
flight_data = FlightData()
for row in sheet_data:
    if flight_data.check(row) is None:
        flight_data.stop_overs=1
        flight_data.check(row)
pprint(sheet_data)




#sheety.print_data()