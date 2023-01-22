# from django.shortcuts import render
import requests

# Create your views here.
def weather(request):
  api_key = 'd17a1f5e7da5101c9409e9f5747b6c64'
  location = ''

  weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

  response = requests.get(weather_url)
  data = response.json()