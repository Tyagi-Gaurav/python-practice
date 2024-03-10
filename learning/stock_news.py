import json
import os
import smtplib

import requests
import datetime as dt
from datetime import timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get the list of user's
env_var = os.environ

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
daily_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": ""  # os.environ["ALPHAVANTAGE_API_KEY"]
}

# response = requests.get(f"https://www.alphavantage.co/query", daily_params)


with open('stock_data.json', 'r') as f:
    response = json.load(f)  # response.json()
date1 = dt.datetime.today().date() - timedelta(days=4)
date2 = dt.datetime.today().date() - timedelta(days=6)

yesterdays_closing_price = float(response.get("Time Series (Daily)")[str(date1)]["4. close"])
day_before_yesterdays_closing_price = float(response.get("Time Series (Daily)")[str(date2)]["4. close"])


def percentage_difference(price1: float, price2: float):
    return abs(price1 - price2) / ((price1 + price2) / 2) * 100


percentage_diff = percentage_difference(yesterdays_closing_price, day_before_yesterdays_closing_price)
if percentage_diff > 5:
    params = {
        "q": "tesla",
        "from": str(date2),
        "sortBy": "publishedAt",
        "apiKey": "" #From os.environ["NEWS_API_KEY"]
    }
    response = requests.get("https://newsapi.org/v2/everything", params)
    news = response.json()
    articles = news.get("articles")
    top_three_headlines = [f"Headline : {article['title']}\nDetail : {article['url']}\n\n" for article in articles[:3]]
    print(top_three_headlines)
    contents = f"🔺{str(round(percentage_diff, 2))}\n"
    contents = contents + "".join(top_three_headlines)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
email = "chonku@gmail.com"
password = ("")  # Get password from chrome password manager for my_python_com

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs="gaurav.tyagi@toptal.com",
                        msg=f"Subject:News Alert\n\n {contents}".encode('utf-8'))

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
