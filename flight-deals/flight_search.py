import requests
API_KEY_KW = "l_ORBhPYztXlwh8hCBlMwb080m6-hp1N"
tequiala_endpoint = "https://tequila-api.kiwi.com/locations/query"
header = {
    "apikey":API_KEY_KW,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def update(self,city_name):
        param = {
            "term": city_name,
            "location_types": "city"
        }
        self.response = requests.get(url=tequiala_endpoint, params=param, headers=header)
        data = self.response.json()
        for ita in data["locations"]:
            return ita["code"]
        #print(data)
        # for ita in self.name:
        #     self.iata.append("TESTING")
