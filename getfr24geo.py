import httplib2 as http
import json
from urllib.parse import urlparse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

balance = 'https://www.flightradar24.com/balance.json'
fr24 = 'http://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=35.53,20.25,136.04,153.59&adsb=1&mlat=1&faa=1&flarm=1&estimated=1&air=1&gnd=1&vehicles=1&gliders=1&array=1'

#target = urlparse(balance)
target = urlparse(fr24)
method = 'GET'
body = ''

h = http.Http()

response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)

data = json.loads(content)

print(data)
