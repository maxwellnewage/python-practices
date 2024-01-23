"""
Stock Price Movement Manager
"""

import requests
from projects.config.globals import ALPHA_VANTAGE_API_KEY, NEWS_API_KEY
from level_intermediate import email

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
DIFF_AMOUNT_ALERT = 1

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stock_info():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    return [value for (key, value) in data.items()]


def get_diff_percent(yesterday, day_before_yesterday):
    difference = abs(yesterday - day_before_yesterday)

    return (difference / yesterday_closing_price) * 100


def get_news():
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    return response.json()["articles"][:3]


if __name__ == '__main__':
    data_list = get_stock_info()

    yesterday_closing_price = float(data_list[0]['4. close'])
    day_before_yesterday_closing_price = float(data_list[1]['4. close'])
    diff_percent = get_diff_percent(yesterday_closing_price, day_before_yesterday_closing_price)

    if diff_percent > DIFF_AMOUNT_ALERT:
        news = get_news()

        for n in news:
            email_message = email.build_message(
                f"{n['title']} | {n['author']}",
                n['description']
            )

            email.send(email_message)
