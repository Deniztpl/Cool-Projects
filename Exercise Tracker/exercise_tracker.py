import requests
import datetime
import os

GENDER = 'male'
WEIGHT = 68
HEIGHT = 183
AGE = 22

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["NT_APP_ID"]
APP_KEY = os.environ["NT_APP_KEY"]

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

params = {
    'query': input("Tell me which exercises you did: "),
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=exercise_headers)
exercise_data = response.json()
exercise_list = exercise_data['exercises']
today = datetime.datetime.now()

for exercise in exercise_list:
    new_row = {
        'workout': {
            'date': today.strftime("%d/%m/%Y"),
            'time': today.strftime("%H:%M:%S"),
            'exercise': exercise["name"].title(),
            'duration': round(exercise["duration_min"]),
            'calories': round(exercise["nf_calories"])
        }
    }
    headers = {"Authorization": f"Basic {os.environ["SH_TOKEN"]}"}
    response = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=headers)
    print(response.text)