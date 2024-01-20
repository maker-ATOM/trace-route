import requests

def getGeoLocation(IP=None):
    if IP is None: 
        response = requests.get(f'http://ip-api.com/json/').json()
    else:
        response = requests.get(f'http://ip-api.com/json/{IP}').json()

    if response['status'] == 'success':
        lat = response['lat']
        lon = response['lon']
        city = response['city']
    elif response['status'] == 'fail':
            lat = None
            lon = None
            city = None
    return(response['status'], IP, (lat, lon), city)