from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.


def RainFall(request):
    r = requests.get('https://api.darksky.net/forecast/547ec77acd0065e31fe87e469c09375e/51.5074,0.1278') # NOQA
    r = r.json()
    rainfall = r['minutely']
    rainfall_data = rainfall['data']
    predictions = []
    for rain in range(1, 6):
        if rainfall_data[rain]['precipProbability'] < 0.25:
            predictions.append('It wont rain in the next {0} mins '.format(rain))# NOQA
        elif 0.75 > rainfall_data[rain]['precipProbability'] >= 0.25:
            predictions.append('It may rain in the next{0} mins '.format(rain))
        else:
            predictions.append('It will rain in the next{0} mins '.format(rain)) # NOQA
    return HttpResponse(predictions)
