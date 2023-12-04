import tkinter as tk
import requests

# Function to retrieve weather data
def getWeather(city):
    print(f"Søger efter vejret i {city}...")
    url = f"https://api.weatherstack.com/current?access_key=f80abd00708e72ed042f3f6af77c5fab&query={city}"
    response = requests.get(url)
    print(response)
    json = response.json()['current']
    print(json)

root = tk.Tk()
root.title("Vejr App")
root.geometry("400x400")

# Label for city
cityLabel = tk.Label(text="City")
cityLabel.place(x=10, y=10)

# Input field to sumbit a city
city = tk.Entry(root, width=20)
city.place(x=100, y=10)

# Button to submit city
submitCity = tk.Button(text="Submit", command=lambda: getWeather(city.get()))
submitCity.place(x=200, y=10)

tk.mainloop()
