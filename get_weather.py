import requests

def get_history_weather(data: dict) -> str:

    response = requests.get(params = data, url = "http://api.weatherapi.com/v1/history.json")
    r_json = response.json()

    weather = "-" * 60 + '\n'

    for key in r_json["location"]:
        if key == "name" or key == "region" or key == "country":
            weather += f"{key.title()}: {r_json['location'][key]}\n"
    
    weather += "-" * 60
    for key in r_json["forecast"]["forecastday"][0]:
        if key == "date":
            weather += f"\nDate: {r_json['forecast']['forecastday'][0][key]}\n"
        if key == "day":
            weather += f"\nTemperature AVG: {r_json['forecast']['forecastday'][0][key]['avgtemp_c']}°\n"
            weather += f"Wind MAX: {round(r_json['forecast']['forecastday'][0][key]['maxwind_kph'] / 3.6, 2)} m/s\n"
            weather += f"\nPrecipitation: {r_json['forecast']['forecastday'][0][key]['totalprecip_mm']} mm\n"
            weather += f"Condition: {r_json['forecast']['forecastday'][0][key]['condition']['text']}\n"
    
    weather += "-" * 60 + f"\nLocaltime: {r_json['location']['localtime']}\n" + "-" * 60

    return weather

def get_current_weather(data: dict) -> str:

    response = requests.get(params = data, url = "http://api.weatherapi.com/v1/current.json")
    r_json = response.json()

    weather = "-" * 60 + '\n'

    for key in r_json["location"]:
        if key == "name" or key == "region" or key == "country":
            weather += f"{key.title()}: {r_json['location'][key]}\n"
    
    weather += "-" * 60
    weather += f"\nTemperature: {r_json['current']['temp_c']}°\n"
    weather += f"Feels Like: {r_json['current']['feelslike_c']}°\n"
    weather += f"\nWind: {round(r_json['current']['wind_kph'] / 3.6, 2)} m/s\n"
    weather += f"Wind Direction: {r_json['current']['wind_dir']}\n"
    weather += f"\nPrecipitation: {r_json['current']['precip_mm']} mm\n"
    weather += f"Condition: {r_json['current']['condition']['text']}\n"
    weather += f"Humidity: {r_json['current']['humidity']}%\n"
    weather += "-" * 60 + f"\nLocaltime: {r_json['location']['localtime']}\n" + "-" * 60

    return weather

def get_forecast_weather(data: dict, days: int) -> str:

    response = requests.get(params = data, url = "http://api.weatherapi.com/v1/forecast.json")
    r_json = response.json()
    weather = "-" * 60 + '\n'

    for key in r_json["location"]:
        if key == "name" or key == "region" or key == "country":
            weather += f"{key.title()}: {r_json['location'][key]}\n"
    
    for day in range(days):
        weather += "-" * 60
        for key in r_json["forecast"]["forecastday"][day]:
            if key == "date":
                weather += f"\nDate: {r_json['forecast']['forecastday'][day][key]}\n"
            if key == "day":
                weather += f"\nTemperature AVG: {r_json['forecast']['forecastday'][day][key]['avgtemp_c']}°\n"
                weather += f"Wind MAX: {round(r_json['forecast']['forecastday'][day][key]['maxwind_kph'] / 3.6, 2)} m/s\n"
                weather += f"\nPrecipitation: {r_json['forecast']['forecastday'][day][key]['totalprecip_mm']} mm\n"
                weather += f"Condition: {r_json['forecast']['forecastday'][day][key]['condition']['text']}\n"
    
    weather += "-" * 60 + f"\nLocaltime: {r_json['location']['localtime']}\n" + "-" * 60
    return weather 