import requests
from datetime import datetime,timezone
import smtplib,time

MY_LAT = 41.683560
MY_LONG=24.292580
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
is_position = (latitude,longitude)
print(is_position)

parameters ={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
time_now = datetime.now(timezone.utc)
def is_it_up():
    if MY_LAT-5<=latitude<=MY_LAT+5 and MY_LONG-5<=longitude<=MY_LONG+5:
        return True
    else:
        return False

def time_dark():
    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True


print(is_it_up(),time_dark())
print(time_now.hour)
while True:

    if is_it_up() and time_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="darimachine6@gmail.com", password="******")
            connection.sendmail(from_addr="darimachine6@gmail.com", to_addrs="serhi1334@gmail.com",
                                    msg="Subject: LOOK UP\n\n There is")
    time.sleep(60)