from geopy.geocoders import Photon
import requests
geolocator = Photon(user_agent="measurements")

# outfit_reccs_map
outfit_reccs_map = {
  "sunny": "Shorts, T-shirt, Light clothing, Sunglasses",
  "cold":  "Sweaters, Jackets, Thick Pants",
  "rainy": "Raincoat, Umbrella, Boots, Thick Clothing",
  "windy": "Jacket, Wind-breaker",
  "snowy": "Warm coat, Gloves, Snow boots"
}

#############################################################
# Functions
#############################################################
# get_latlong_location
def get_latlong_location(address):
  print(f"get_latlong({address})")
  return geolocator.geocode(address)

# make_api_get_request
def make_api_get_request(url):
  response = requests.get(url)
  if response.status_code == 200:
      data = response.json()
      return data
  else:
      print('Failed to retrieve data:', response.status_code)

# get_forecast_api_url
# example call https://api.weather.gov/points/37.7011,-121.8676
def get_forecast_api_url(location):
  latitude = location.latitude
  longitude = location.longitude
  points_api_url = f"https://api.weather.gov/points/{latitude},{longitude}"
  response = make_api_get_request(points_api_url)
  if response:
    return response["properties"]["forecast"]
  return None

# get_forecast
def get_forecast(forecast_api_url):
  response = make_api_get_request(forecast_api_url)
  if response:
    return response["properties"]["periods"]
  return None

# get_next_3day_forecast()
def get_next_3day_forecast(forecast_api_url):
  full_forecast = get_forecast(forecast_api_url)
  # Note: A full forecast includes both day and night entries
  #  so we removed entries with names that include night
  #  and take first 3 entries from the result list     
  threeday_forecast = []
  for x in full_forecast:
    entry_name = x["name"].lower()
    if "night" not in entry_name:
      threeday_forecast.append(x)
  return threeday_forecast[:3]

# get_outfit_reccs
# Below is the logic used by recommender
# =============================================================
#   Sunny and warm: Suggest shorts, T-shirt, and sunglasses.
#     > 72
#     Search for “Sunny”
#   Cold:  Suggest a Sweater, Jackets and thick pants
#     <= 72
#     Search for “Cold”
#   Rainy: Suggest a raincoat, umbrella, and boots.
#     Search for “Rain”
#   Windy : Suggest a Jacket, Hoodie
#     Search for “Wind” or “Gust”
#   Snowy: Suggest a warm coat, gloves, and snow boots.
#     Search for “Snow”
# =============================================================
def get_day_outfit_reccs(weather_info):  
  reccs = {}
  # Sunny and warm:
  if "temperature" in weather_info and weather_info["temperature"] > 72:
    reccs["sunny"] = outfit_reccs_map["sunny"]
  elif "temperature" in weather_info and weather_info["temperature"] <= 72:
    reccs["cold"] = outfit_reccs_map["cold"]

  if "detailedForecast" in weather_info:
    weather_text = weather_info["detailedForecast"].lower()
    if "rain" in weather_text:
      reccs["rainy"] = outfit_reccs_map["rainy"]
    if "wind" in weather_text or "gust" in weather_text:
      reccs["windy"] = outfit_reccs_map["windy"]
    if "snow" in weather_text:
      reccs["snowy"] = outfit_reccs_map["snowy"]
  #return
  return {
    "date": weather_info["startTime"][5:7] + "/" + weather_info["startTime"][8:10] + "/" + weather_info["startTime"][:4],
    "week": weather_info["name"].split(" ")[0],
    "weather": " and ".join(list(reccs.keys())),
    "outfit_reccs": ", ".join(list(reccs.values())) 
  }

def get_reccs_by_location(location_info):
  # get geo locatoon info
  location = get_latlong_location(location_info)

  # call get_forecast_points_api_url to get forecast api URL
  # example call: https://api.weather.gov/gridpoints/MTR/103,98/forecast
  forecast_api_url = get_forecast_api_url(location)
  #print(forecast_api_url)

  # call get_forecast to get forecast 
  forecast_info = get_next_3day_forecast(forecast_api_url)
  #for x in forecast_info:
  #  print(x)
  reccs = []
  for x in forecast_info:
    reccs.append(get_day_outfit_reccs(x))
  
  # return
  return reccs

#############################################################
# Main
#############################################################
if __name__ == "__main__":
  location_name = input("Enter your City Name :")
  reccs = get_reccs_by_location(location_name)
  for x in reccs:
    print('.'*70)
    print(x)

  # Run this to prepare requirements.txt
  # pip3 freeze .\recomender.py > requirements.txt


