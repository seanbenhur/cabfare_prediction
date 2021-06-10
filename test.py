import requests
import json

# local url
url = 'http://127.0.0.1:5000'

#data
data = {'cab_provider': 3
      , 'source': 2
      , 'destination': 1
      , 'distance': 50,
      'surge_multiplier': 1.0,
      'cab_type': 3}

data = json.dumps(data)

send_request  = requests.post(url,data)
print(send_request.json())