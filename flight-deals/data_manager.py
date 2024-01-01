import requests
from pprint import pprint
sheet_endpoint_price = "https://api.sheety.co/d572c48f425769727bb75a0fe656a3dc/flightDeals/prices"
sheet_endpoint_user = "https://api.sheety.co/d572c48f425769727bb75a0fe656a3dc/flightDeals/users"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.response = requests.get(url=sheet_endpoint_price)
        self.data = self.response.json()

    def update_sheet(self,sheet_data):
        for data in sheet_data:
            print(data)
            id = data["id"]
            print(id)
            ita = data["iataCode"]
            print(ita)
            put_parameters={
                "price":{
                    "iataCode":ita
                }
            }
            self.response_update = requests.put(url=f"{sheet_endpoint_price}/{id}", json=put_parameters)
            #print(self.response_update.text)
    def user_information(self):
        print("Welcome to Serhan's Fligh Club.\n We find the best flight deals and email you.")
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        user_email = input("What is your email?\n")
        user_email_check = input("Type your email again.\n")
        if user_email==user_email_check:
            param = {
                "user":{
                    "firstName": first_name,
                    "lastName":last_name,
                    "email":user_email,
                }

            }

            user_respone = requests.post(url=sheet_endpoint_user,json=param)
            print("You are in the club!")
            print(user_respone.text)

