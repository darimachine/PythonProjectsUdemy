from pprint import pprint

import requests
import datetime
MY_CITY_CODE = "SOF"
API_KEY_KW = "l_ORBhPYztXlwh8hCBlMwb080m6-hp1N"
search_endpoint = "https://tequila-api.kiwi.com/v2/search"
header = {
    "apikey":API_KEY_KW,
}
today = datetime.datetime.now() + datetime.timedelta(days=1)
end_day = today + datetime.timedelta(days=185)
today = today.strftime('%d/%m/%Y')
end_day = end_day.strftime('%d/%m/%Y')
print(today)
print(end_day)
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.stop_overs=0
        self.via_city=""
    def check(self,row):
        param = {
            "fly_from": MY_CITY_CODE,
            "fly_to":row['iataCode'],
            "date_from": today,
            "date_to":end_day,
            "curr":"EUR",
            "flight_type":"round",
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "max_stopovers":0,
            "one_for_city":1

        }
        try:
            self.response = requests.get(url=search_endpoint,params=param,headers=header)
           
            data = self.response.json()["data"][0]
        except:
            print(f"No flight found for {row['city']}")


            return None
        else:
            param["max_stopovers"] = 0
            country = data["route"][0]["cityTo"]
            money = data["price"]
            out_date = data["route"][0]["local_departure"].split("T")[0]
            return_date = data["route"][1]["local_departure"].split("T")[0]
            # # deep_link = data["deep_link"]
            pprint(f"{country} - {money}")
            pprint(data["route"][0])
