#!/usr/bin/python3

from display import *
from gethelp import *
from geolocation import *
from route import *
import sys
import socket

if len(sys.argv)!=2:
    printHelp()
    exit()

# Get hostname
hostname = sys.argv[1]
try:
    target_ip = socket.gethostbyname(hostname)
except:
    print("Enter valid Hostname")
    exit()

# Trace ips in the path
route = traceroute(target_ip)

# Get geolocation of ips
geolocations = []
print()
for ip in route:
    location = getGeoLocation(ip)
    if location[0] == 'success':
        print(f'{location[1]} at {location[3]}')
        geolocations.append(location)
print()

if geolocations[-1][1] == target_ip:
    print("Destination reached...")
else:
    print("Desination did not reached, try again...")
print()

# Extract the data
cities = tuple(city for _, _, _, city in geolocations)
lats = tuple(coord[0] for _, _, coord, _ in geolocations)
longs = tuple(coord[1] for _, _, coord, _ in geolocations)

# Ptot the route 
fig = go.Figure()
mapsInit(fig)

addRoute(fig, lats, longs, cities)

destination = getGeoLocation(target_ip)
addNode(fig, destination[2][0], destination[2][1], destination[3], 'destination')

source = getGeoLocation()
addNode(fig, source[2][0], source[2][1], source[3], 'source')

fig.show()