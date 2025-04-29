import requests
from datetime import datetime

"""
MY_LAT=51.507351
MY_LONG =-0.127758
"""

#---------------------------------iss_position---------------------------
"""
response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response) # Tells us if the request succeeded or not. 1XX = Hold on (something happening this is not final)
                 #2XX = Here you go everything is succeful ; 3XX = Go Away - you don't have any permission 4XX = You screwed up - the thing you are looking for it doesn't exist
                 #5XX = I(the server) screwed up - maybe the server/website is down
print(response.status_code)#returnes only the number that indicate the status of the site

if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data.")
    
#----option 2 : for make an error in the contact to the site---- :
# response.raise_for_status()
# print("response.raise_for_status() : ", response.raise_for_status())

#data = response.json()
data = response.json()["iss_position"]

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
print(f"iss_position: latitude:{latitude} , longitude:{longitude}")

"""


#-------------------------------Example about kanye -----------------------------


response = requests.get(url="https://api.kanye.rest")

data =response.json()

print(data["quote"])




#----------------------- Example about sun ---------------------------------------
"""
# sunrise and sunsite time
MY_LAT = 32.794044
MY_LONG = 34.989571

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
# print("response.raise_for_status() : ", response.raise_for_status())
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
# print(data["results"])
# print("Sunrise time : " , sunrise)
# print("Sunset time : " , sunset)
# print("Sunrise time : " ,sunrise.split("T"))
print("Sunrise time in Haifa: ", sunrise.split("T")[1])
# print("Sunrise time : " , sunrise.split("T")[1].split(":"))
print("Sunset time in Haifa: ", sunset.split("T")[1])
# print(sunrise.split("T")[1].split(":")[0])


time_now = datetime.now()
print("The current date + time in the current time zone : ", time_now)
"""

