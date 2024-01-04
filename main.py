from dotenv import load_dotenv
from get_weather import get_current_weather, get_forecast_weather, get_history_weather
from validate_data import get_location, check_exit, get_time_range, get_weather_date
from datetime import date, timedelta
import os

def main():

    load_dotenv(".env")
    WEATHER_API_TOKEN = os.getenv("WEATHER_API_TOKEN") # https://www.weatherapi.com/

    while True:
        os.system("cls")

        print("Anytime type Exit to exit the program!")
        location = get_location(WEATHER_API_TOKEN)
        time_range = get_time_range()

        match time_range:
            case "history":
                data = {
                    "key": WEATHER_API_TOKEN,
                    "q": f"{location}",
                    "dt": f"{date.today() - timedelta(days = get_weather_date())}"
                }
                weather = get_history_weather(data)
            case "current":
                data = {
                    "key": WEATHER_API_TOKEN,
                    "q": f"{location}"
                }
                weather = get_current_weather(data)
            case "forecast":
                days = 3
                data = {
                    "key": WEATHER_API_TOKEN,
                    "q": f"{location}",
                    "days": f"{days}"
                }
                weather = get_forecast_weather(data, days)

        os.system("cls")
        print(weather)
        check_exit(input("\nPress <ENTER> to continue: "))

if __name__ == "__main__":
    main()
    os.system("cls")

