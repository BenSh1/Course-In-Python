import smtplib

import datetime as dt
import random


"""
my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user= my_email, password=password)

connection.sendmail(
        from_addr=my_email , 
        to_addrs="shar.ben@yahoo.com" , 
        msg="Subject:Hello\n\nThis is the body of the email."
    )


connection.close()
"""


"""
my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()

    connection.login(user= my_email, password=password)

    connection.sendmail(
        from_addr=my_email , 
        to_addrs="shar.ben@yahoo.com" , 
        msg="Subject:Hello\n\nThis is the body of the email."
    )


"""


"""
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(month)

date_of_birth = dt.datetime(year=1996 , month=4 , day=24 )
print(date_of_birth)

"""


my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas"

now = dt.datetime.now()
current_day = now.weekday()


#if current_day == 1:#if the weekday is monday==1
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.read().splitlines()
    random_quote = random.choice(all_quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)

    connection.sendmail(
                from_addr=my_email , 
                to_addrs="shar.ben@yahoo.com" , 
                msg=f"Subject:Daily Motivation\n\n{random_quote}"
            )

