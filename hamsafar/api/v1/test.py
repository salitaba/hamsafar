from urllib.request import urlopen, Request
import requests
import json
validated_data = {
    "start_lat": "47.217954",
    "start_long": "-1.552918",
    "end_lat": "47.217954",
    "end_long": "-1.552918",
}
url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={}&lon={}".format(
    validated_data['end_lat'], validated_data['end_long'])
print(url)

headers = {
    'Host': 'nominatim.openstreetmap.org',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}
# url = "http://google.com/"
# response = urlopen(url)

# request.open
# response = urllib.urlopen(url)
# print(response.read())
print("*" * 100)
# req = Request(url=url, headers=headers)
req = requests.get(url)

# html = urlopen(req)
# data = json.loads(html)
data = json.loads(req.content.decode('utf-8'))
validated_data['end_road'] = data['address']['road']

print(data['address']['road'])
