import requests
import os
from twilio.rest import Client
MY_LAT = 41.683560
MY_LONG=24.292580
API_KEY = "f5e624636ba4bfc5461db6b76ceaeb47"
account_sid = "AC64e30bbeafda910c62fa777527412c4b"
auth_token = os.environ.get("OWM_AUTH_TOKEN")

#https://api.openweathermap.org/data/2.5/weather?lat=41.683560&lon=24.292580&appid=f5e624636ba4bfc5461db6b76ceaeb47
#https://api.openweathermap.org/data/2.5/weather?q=Borino,BG&appid=f5e624636ba4bfc5461db6b76ceaeb47
#one call api
#https://api.openweathermap.org/data/2.5/onecall?lat=41.683560&lon=24.292580&appid=f5e624636ba4bfc5461db6b76ceaeb47
#full data
f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&appid={API_KEY}"
parameters ={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "exclude":"current,minutely"
}
print(os.environ)
client = Client(account_sid, auth_token)
message = client.messages.create(body="Shte vali", from_="+19786783260", to="+359877794630")
print(message.status)
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data["hourly"]
weather_data = weather_data[:12]
print(weather_data)
will_rain=False
for i in weather_data:
    weather_id = i["weather"][0]["id"]
    if int(weather_id)<700:
        will_rain = True

if will_rain:

    print("Bring Umbrella")
