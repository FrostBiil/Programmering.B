import tkinter as tk
import requests
from abc import ABC, abstractmethod

bg_color = "#fff"
fg_color = "#000"

# Function to retrieve weather data
def getWeather(city):
    print(f"Søger efter vejret i {city}...")
    url = f"http://api.weatherstack.com/current?access_key=52d40b52fa3de13f3e4f4692fbb455fd&query={city}"
    response = requests.get(url)
    print("Response Status Code:", response.status_code)
    
    global data
    data = response.json()['current']
    print("API Response:", data)

    if 'current' in data:
        current_weather = data['current']
        print(current_weather)
    else:
        print("Error: 'current' key not found in response. Response content:", data)

def updateWeatherLabels(city, temp, wind, windDir):
    cityLabel.config(text=city)
    tempLabel.config(text=f"Temperatur: {temp} C\u00b0")
    windLabel.config(text=f"Vindhastighed: {wind} m/s")
    windDirLabel.config(text=f"Vindretning: {windDir}")

def kmToMph(temp):
    return temp * 0.277778
    

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class GetWeatherCommand(Command):
    def __init__(self, city):
        self.city = city

    def execute(self):
        getWeather(self.city)
        updateWeatherLabels(self.city, data['temperature'], kmToMph(data['wind_speed']), data['wind_dir'])


    

root = tk.Tk()
root.title("Vejr App")
root.geometry("900x900")

# Background image
background_image = tk.PhotoImage(file="map.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Compas image
compas_image = tk.PhotoImage(file="kompas1.png")
compas_label = tk.Label(root, image=compas_image)
compas_label.place(x=590, y=160)

# Label for city
enterCityLabel = tk.Label(root, text="Indtast en by: ", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
enterCityLabel.place(x=10, y=10)

# Input field to submit a city
city = tk.Entry(root, width=12, font=("Helvetica", 12))
city.place(x=10, y=40)

# Button to submit city
submitCity = tk.Button(root, text="Enter", command=lambda: GetWeatherCommand(city.get()).execute(), width=10, font=("Helvetica", 12))
submitCity.place(x=10, y=70)
submitCity.config(bg=bg_color, fg=fg_color)

# Label for weather data
cityLabel = tk.Label(root, text="Vælg venligst en by", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
cityLabel.place(x=600, y=10)

# Lavel for temperature
tempLabel = tk.Label(root, text="Temperatur: ", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
tempLabel.place(x=600, y=50)

# Label for wind speed
windLabel = tk.Label(root, text="Vindhastighed: ", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
windLabel.place(x=600, y=80)

# Label for wind direction
windDirLabel = tk.Label(root, text="Vindretning: ", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
windDirLabel.place(x=600, y=110)

tk.mainloop()
