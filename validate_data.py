import requests
import os
import sys
from time import sleep

def get_location(WEATHER_API_TOKEN: str) -> str:
    while True:
        location = input("\nEnter Location: ").lower()
        
        check_exit(location)

        r = requests.get(params = {"key": WEATHER_API_TOKEN, "q": f"{location}"}, url = "http://api.weatherapi.com/v1/current.json")

        if r.status_code != 200:
            print("Unknown Location!")
            continue

        return location

def get_time_range() -> str:
    while True:
        time_range = input("\nHistory | Current | Forecast: ").lower()
        check_exit(time_range)
        if time_range != "history" and time_range != "current" and time_range != "forecast":
            print("Unknown Time Range!")
            continue
        return time_range

def get_weather_date() -> int:
    while True:
        weather_date = input("\n(1-7) How many days ago?: ").lower()
        check_exit(weather_date)
        try:
            weather_date = int(weather_date)
            if weather_date < 1 or weather_date > 7:
                print("Too Far!")
                continue
        except ValueError:
            print("Input must be a number!")
            continue
        return weather_date

def check_exit(user_input: str) -> None:
    if user_input.lower() == "exit":
        os.system("cls")
        print("Thanks for using the program!")
        sleep(0.5)
        os.system("cls")
        sys.exit()
