import time
import requests
from datetime import datetime
import smtplib


MY_LAT = 32.766948 # Your latitude
MY_LONG = 35.011429 # Your longitude
my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+ 5 and MY_LONG - 5<= iss_longitude <= MY_LONG + 5:
        return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
"""

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night() :
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email, password=password)

            connection.sendmail(
                        from_addr=my_email , 
                        to_addrs="shar.ben@yahoo.com" , 
                        msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
                    )

   

"""
 
if is_iss_overhead() and is_night() :
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)

        connection.sendmail(
                        from_addr=my_email , 
                        to_addrs="shar.ben@yahoo.com" , 
                        msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
                    )

   