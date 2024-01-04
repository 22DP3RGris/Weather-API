# Weather-API

This is a weather information console  application that uses the Weather API. It allows users to retrieve current, forecast, and historical weather data for a specific location.

## How it looks

- History
  
  ![Hisotry](/img/history.png)

- Current
  
  ![Current](/img/current.png)

- Forecast
   
  ![Forecast](/img/forecast.png)

## How to Install & Use


Download the repository:
``` Bash
git clone https://github.com/22DP3RGris/Weather-API.git
```

Navigate to the project directory:
``` Bash
cd Weather-API
```

Open ".env" and put your own API token:
``` sh
WEATHER_API_TOKEN = "Your Weather API token" 
```

Download "requests" module:
``` Bash
pip install requests
``` 

After installing the necessary dependencies and setting up your API token, you can run the application using Python:

```bash
python main.py
```

## Get API token

1. Visit [WeatherAPI](https://www.weatherapi.com/).
   
2. Click on the "Sign Up" button.
   
3. Fill out the registration form with your details and click "Create My Account".
   
4. You will receive an email to verify your account. Click on the link in the email to verify your account.
   
5. After verifying your account, log in to WeatherAPI.
   
6. You will be redirected to your dashboard. Here, you can see your API key. This is the token you will use in the application.