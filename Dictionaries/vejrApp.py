import tkinter as tk
import requests

# Function to retrieve weather data
def getWeather(city):
    print(f"Søger efter vejret i {city}...")
    url = f"http://api.weatherstack.com/current?access_key=52d40b52fa3de13f3e4f4692fbb455fd&query={city}"
    response = requests.get(url)
    print("Response Status Code:", response.status_code)
    
    data = response.json()
    print("API Response:", data)

    if 'current' in data:
        current_weather = data['current']
        print(current_weather)
    else:
        print("Error: 'current' key not found in response. Response content:", data)


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
