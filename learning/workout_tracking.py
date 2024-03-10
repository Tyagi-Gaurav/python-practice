# Updating Google sheets
import requests
from datetime import datetime as dt

APP_ID = ""
API_KEY = ""

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("Tell me what exercise(s) you did today? ")
}

response = requests.post(url, json=body, headers=headers)
exercises = response.json()["exercises"]
sheet_url = "https://api.sheety.co/3a70872e35e94b37f72beacdea0fa550/myWorkouts/workouts"
for json in exercises:
    body = {
        "workout": {
            "date": dt.now().strftime("%d/%m/%Y"),
            "time": "00::00:00",
            "exercise": json.get("user_input"),
            "duration": json.get("duration_min"),
            "calories": json.get("nf_calories")
        }
    }
    sheet_response = requests.post(sheet_url, json=body)

