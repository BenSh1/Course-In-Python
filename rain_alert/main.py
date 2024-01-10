import json
import requests
import smtplib


my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas"


OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "87e12a9916e0ed12cf144ba6f16aedf6"
MY_LAT = 32.79
MY_LONG = 34.98

weather_params = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "cnt":4
}

#response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
#response = requests.get(url=OMW_Endpoint, params=weather_params)
response = requests.get(OMW_Endpoint, params=weather_params)

#print(response.status_code)
#print(response)

response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])
#print(data)


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"] 
    if int(condition_code) < 700 :
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user= my_email, password=password)

        connection.sendmail(
            from_addr=my_email , 
            to_addrs="shar.ben@yahoo.com" , 
            msg="Subject:Need an umbrella \n\nIt's going to rain today. Remember to bring an umbrella!"
        )


