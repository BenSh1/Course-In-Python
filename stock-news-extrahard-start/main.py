import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

OMW_ENDPOINT_STOCK_PRICE = "https://www.alphavantage.co/query"
STOCK_PRICE_API_KEY = "LB8F4A9KDRQEO8HE"

OMW_ENDPOINT_STOCK_NEWS = "https://newsapi.org/v2/everything"
STOCK_NEWS_API_KEY = "b5c2c68d0e3440079f9db5202996fbc2"

my_email = "sben199604@gmail.com"
password = "kixxfvzjobbmwjaz"

price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


response_stock_price = requests.get(OMW_ENDPOINT_STOCK_PRICE, price_params)
data_price = response_stock_price.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data_price.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    news_params = {
        # "q": COMPANY_NAME,
        "apiKey": STOCK_NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    response_stock_news = requests.get(OMW_ENDPOINT_STOCK_NEWS, params=news_params)
    data = response_stock_news.json()
    articles = data["articles"]

    """
    # I want only 3 articles that the title and the description is both not define as None 
    i = 0
    three_articles_ben = []
    count_in_three_articles = 0
    while i < len(articles):
        print(f" title: {articles[i]['title']}\ndescription: {articles[i]['description']}")

        #if not articles[i]["title"] and not articles[i]["description"]:
        if articles[i]["title"] and articles[i]["description"]:
            three_articles_ben.append(articles[i])
            count_in_three_articles += 1
        print("count_in_three_articles : " , count_in_three_articles)
        if count_in_three_articles == 3:
            break
        i += 1

    print("The 3 articles about Tesla: ", three_articles_ben)
    """
    three_articles = articles[:3]
    print("The 3 articles about Tesla: ", three_articles)

    formatted_articles = [
        f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]

    """
    for article in formatted_articles:
        # Create MIME-formatted email
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = "ben1364@gmail.com"
        msg['Subject'] = "Daily News Update"
        msg.attach(MIMEText(article, "plain", "utf-8"))  # Ensures UTF-8 encoding

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs="ben1364@gmail.com",
                msg=msg.as_string()
            )
            print("The mail has been sent to the email - ben1364@gmail.com")

    """

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
