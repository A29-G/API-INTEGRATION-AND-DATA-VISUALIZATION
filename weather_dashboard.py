import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = "18c89b11bc05ad4c8e85435c0255fea3"
CITY = "Delhi"
UNITS = "metric"

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None

def process_data(weather_data):
    dates = []
    temperatures = []
    
    for item in weather_data['list']:
        dt_txt = item['dt_txt']
        temp = item['main']['temp']
        dates.append(datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S'))
        temperatures.append(temp)
    
    return dates, temperatures

def visualize(dates, temperatures):
    plt.figure(figsize=(12,6))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='skyblue')
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Fetching weather data...")
    data = fetch_weather_data(CITY)
    if data:
        dates, temps = process_data(data)
        visualize(dates, temps)
