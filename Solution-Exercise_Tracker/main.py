import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 1.65
AGE = 27

APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]
TOKEN = os.environ["ENV_TOKEN"]

exercise_endpoint = os.environ["ENV_EXERCISE_ENDPOINT"]
sheet_endpoint = os.environ["ENV_SHEET_ENDPOINT"]


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
