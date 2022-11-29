from time import sleep
from requests import get
from pprint import pprint

# Obtendo dados do clima
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'

weather = get(url).json()['items']
temperatura = weather[0]["ambient_temp"]
data = weather[0]["created_on"]
created = weather[0]["created_by"]

pprint(temperatura, data, created)
