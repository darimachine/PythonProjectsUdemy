# write yourn own email and password
import pandas as pd
import datetime as dt
import smtplib,random
MY_EMAIL = "darimachine6@gmail.com"
data = pd.read_csv("birthdays.csv")
now = dt.datetime.today()
random_letter = random.randint(1,3)
data = data.to_dict(orient="records")

for i in range(len(data)):
    if now.month==data[i]["month"] and now.day==data[i]["day"]:
        with open(f"letter_templates/letter_{random_letter}.txt") as file:
            letter = file.read()
            letter_real = letter.replace("[NAME]",data[i]["name"])
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password="....")
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=f"{data[i]['email']}",msg=f"Subject:Happy Birthday\n\n{letter_real}")





