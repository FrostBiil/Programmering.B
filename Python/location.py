import geocoder
import requests

def get_user_location():
    try:
        g = geocoder.ip('me')
        return g.city
    except Exception as e:
        return "Unknown"

def get_weather(location):
    try:
        url = f"https://www.dmi.dk/dmidk_byvejrWS/rest/text/{location}/"
        response = requests.get(url)
        data = response.json()
        if data:
            return data[0]['text']
        else:
            return "Weather data not available."
    except Exception as e:
        return "Error fetching weather data."

if __name__ == "__main__":
    user_location = get_user_location()
    print(f"Your location: {user_location}")
    
    if user_location != "Unknown":
        weather = get_weather(user_location)
        print(f"Weather in {user_location}: {weather}")
    else:
        print("Location not available.")

input("Press Enter to exit...")