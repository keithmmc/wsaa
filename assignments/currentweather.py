import requests  # import requests to get API 
import json #import json 
url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"
response = requests.get(url) #request url
data = response.json() #get the response
currentObject = data["current"]
current_temp = currentObject["temperature_2m"]
current_wind = currentObject["wind_speed_10m"]
print("Current temperature = ",current_temp)
print("Current wind direction = ",current_wind) 
