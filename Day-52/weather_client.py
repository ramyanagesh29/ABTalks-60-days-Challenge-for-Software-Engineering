import json
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

def fetch_json(url):
    request = Request(url, headers={"User-Agent": "ABTalksWeatherDemo/1.0"})
    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))

def get_weather(city):
    geo = fetch_json("https://geocoding-api.open-meteo.com/v1/search?name="
                     + quote(city) + "&count=1&language=en&format=json")
    results = geo.get("results", [])
    if not results:
        raise ValueError("No location found for " + city)
    place = results[0]
    url = ("https://api.open-meteo.com/v1/forecast?latitude=" + str(place["latitude"])
           + "&longitude=" + str(place["longitude"])
           + "&current=temperature_2m,relative_humidity_2m,apparent_temperature,"
             "precipitation,wind_speed_10m&timezone=auto")
    current = fetch_json(url).get("current")
    if not current:
        raise ValueError("Weather response has no current conditions")
    return place, current

if __name__ == "__main__":
    city = input("Enter a city (e.g., Mysuru): ").strip()
    if not city:
        print("Please enter a city name.")
    else:
        try:
            place, w = get_weather(city)
            print("\nWeather Intelligence Report")
            print("Location:", place["name"] + ", " + place.get("country", ""))
            print("Temperature:", w.get("temperature_2m"), "°C")
            print("Feels like:", w.get("apparent_temperature"), "°C")
            print("Humidity:", str(w.get("relative_humidity_2m")) + "%")
            print("Wind:", str(w.get("wind_speed_10m")) + " km/h")
            print("Precipitation:", str(w.get("precipitation")) + " mm")
            print("Observation time:", w.get("time"))
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as e:
            print("Could not fetch/process weather data:", e)
            print("Check the city name and internet connection, then retry.")
