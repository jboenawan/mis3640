import urllib.request
import json

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Babson+College"
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data['results'][0]['address_components'][5]['short_name'])