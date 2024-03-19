import json
import requests
import smtplib

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas" # i assume for email in gmail


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CHANGE_PERCENTAGE = 0.2

STOCK_API_KEY = "TBW5O365BWHOXTZ9"
NEWS_API_KEY = "b5c2c68d0e3440079f9db5202996fbc2"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
#print(response.status_code)
#print(response.json())
data_stock = response.json()
#print(data_stock)
#print(data_stock["Time Series (Daily)"])

data_Of_Each_Day = data_stock["Time Series (Daily)"]
data_list = [value for (key,value) in data_Of_Each_Day.items()]

#print(data_list[0])
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
#print("yestrday_closing_price: " ,yesterday_closing_price)

the_day_before_yesterday_data = data_list[1]
the_day_before_yesterday_closing_price = the_day_before_yesterday_data["4. close"]
#print("the_day_before_yesterday_closing_price : " , the_day_before_yesterday_closing_price)



difference = float(yesterday_closing_price) - float(the_day_before_yesterday_closing_price)
#print("difference : " ,difference)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
diff_percent = abs(diff_percent)
#print("diff_percent : ", diff_percent)


if diff_percent > CHANGE_PERCENTAGE:
    news_params = {
        "qInTitle":COMPANY_NAME,
        "apiKey":NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT,news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    #print(three_articles)

    formatted_articles = [f"Healdline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    #print(formatted_articles[1])
    
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("sent via email!")
        connection.starttls()

        connection.login(user= my_email, password=password)

        connection.sendmail(
            from_addr=my_email , 
            to_addrs="shar.ben@yahoo.com" , 
            msg=f"Subject:Change in {COMPANY_NAME} \n\n{STOCK}: {diff_percent} '%\n' {formatted_articles[0]}"
        )

    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""




