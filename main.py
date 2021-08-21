import requests
from datetime import datetime
import os


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/bd595172d576465af66dce4e779b3be8/workouts/workouts"
TOKEN = os.environ.get("TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


input = input("What exercise did you do today? ")


data = {"query": input}

response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, headers=headers, json=data)

response = response.json()["exercises"]

day = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

for res in response:
    exercise = res["name"]
    duration = res["duration_min"]
    calories = res["nf_calories"]

    data = {
        "workout": {"date": day, "time": time, "exercise": exercise.title(), "duration": duration, "calories": calories}
    }

    headers = {"Authorization": TOKEN}

    response = requests.post(url=SHEETY_ENDPOINT, json=data, headers=headers)
