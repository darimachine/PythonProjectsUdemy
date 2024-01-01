import requests
import datetime as dt
import math
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "Q6993K35X5882LII"
NEWS_API_KEY = "515f9a651eb841399c43171f5d64e96c"
parameters_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":STOCK_API_KEY,

}
parameters_news = {
    "q":"tesla",
    "sortBy":"publishedAt",
    "language":"en",
    "apiKey":NEWS_API_KEY,
}
#datetimne right now
now = dt.datetime.now()
year = now.year
month = now.month
day = int(now.day)
hour = int(now.hour)
print(now)
#stock API
response_stock = requests.get(url="https://www.alphavantage.co/query", params=parameters_stock)
response_stock.raise_for_status()
data_json = response_stock.json()
data = data_json["Time Series (Daily)"]
print(data)
#NEWS API

response_news = requests.get(url="https://newsapi.org/v2/everything",params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()
news = data_news["articles"][:3]
print(data_news)
print(news)
repeat = []
#end
#twilio api
client = Client("AC64e30bbeafda910c62fa777527412c4b", "ff7fbbd4f374c1b969cce83ee07f5595")
#end of api
if hour>=23:
    yesterday = data[f"{year}-{month:02d}-{day:02d}"]
    day_before_yesterday = data[f"{year}-{month:02d}-{day - 1:02d}"]
else:
    yesterday = data[f"{year}-{month:02d}-{day-1:02d}"]
    day_before_yesterday = data[f"{year}-{month:02d}-{day-2:02d}"]
yesterday = yesterday["4. close"]
day_before_yesterday= day_before_yesterday["4. close"]
subtract =  round(float(yesterday) - float(day_before_yesterday), 2)

if subtract>0:
    up_emoji = "🔼"
    percentage = math.floor((subtract * 100) / float(yesterday))
else:
    up_emoji = "🔽"
    subtract=abs(subtract)
    percentage = math.floor((subtract * 100) / float(day_before_yesterday))
i = 0
j = 0
while (j < 3):
    if news[i]["author"] not in repeat:
        message = client.messages.create(
            body=f"TSLA: {up_emoji}{percentage}%\n Headline: {news[i]['title']}\n Brief: {news[i]['description']}",
            from_="+19786783260", to="+359877794630")
        repeat.append(news[i]["author"])
        i += 1
        j += 1
        print(message.status)

    else:
        i += 1
print(f"{percentage}%")
# print(yesterday)
# print(day_before_yesterday)
# print(subtract)
## STEP 1: Used https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Used https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Used https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional example: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

