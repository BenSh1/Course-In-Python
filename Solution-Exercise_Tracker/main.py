import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 1.65
AGE = 27

APP_ID = "416d0990"
API_KEY = "f9ba873f10c57258e4b1c2bac69cf45d"
TOKEN = "Bearer BBBBBBBBBBBBBBBBBBBBMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/048d30af9bfbb754298748a72cb289bb/workoutTracking/workouts"

#The input gets sent in the form of: '30 minutes of yoga
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

bearer_headers  = {"Authorization": TOKEN}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=bearer_headers)

    print(sheet_response.text)
