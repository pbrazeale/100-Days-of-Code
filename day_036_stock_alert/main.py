import requests
import values

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": values.alphakey,
}

alpha_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
# print(alpha_response.json())
stock_data = alpha_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_stock_data = stock_data_list[0]
yesterday_closing_price = yesterday_stock_data["4. close"]
# print(yesterday_closing_price)

two_days_ago_data = stock_data_list[1]
two_days_ago_closing_price = two_days_ago_data["4. close"]
# print(two_days_ago_closing_price)

difference = abs(float(yesterday_closing_price) - float(two_days_ago_closing_price))
# print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
# print(diff_percent)


if diff_percent > 3:
    news_parameters = {
        "apiKey": values.newskey,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]

three_articles = articles[:3]
# print(three_articles)

formatted_articles = [
    f"Headline: {article['title']} \nBrief: {article['description']}"
    for article in three_articles
]


# TODO 9. - Send each article as a separate message via Twilio.
if float(yesterday_closing_price) > float(two_days_ago_closing_price):
    for article in formatted_articles:
        print(f"{STOCK_NAME}: 🔺{diff_percent:.2f}%\n{article}")
else:
    for article in formatted_articles:
        print(f"{STOCK_NAME}: 🔻{diff_percent:.2f}%\n{article}")

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
