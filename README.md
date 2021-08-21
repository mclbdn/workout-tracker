# workout-tracker

Workout tracker, written in Python, turning user's written text into exercise analysis(Nutritionix) and writing the date, type of exercise, exercise duration, and calories burned into Google sheets(Sheety).

## Prerequisites
Nutritionix account 
Sheety account
Google account
Requests library (`pip install requests`)  

## Usage

* First, clone the repo:
```
git clone https://github.com/mclbdn/workout-tracker
```
* Then, install the requests library:
```
pip install requests
```
* Create a Google Sheets sheet and connect it to Sheety.
* Set the environment variables for APP_ID(Nutritionix), API_KEY(Nutritionix), and TOKEN(Sheety).
* Run `python3 main.py`.
* Your workout data will be automatically written into created Google sheet.

