import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps

API='AIzaSyCnwdJb9z0rhD6HjpNYQnHvV3ObR644UEI'
geolocator = GoogleV3(api_key=API)
# generating Empire State Building coordinates
name = 'Empire State Building'
location = geolocator.geocode(name)
print(location.address)
print(location.latitude, location.longitude)

first_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]], columns=['name', 'address', 'lat', 'lon'])
print(first_location)
# generating Marea Restaurant New York coordinates
name = 'Marea Restaurant New York'
location = geolocator.geocode(name)
second_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]], columns=['name', 'address', 'lat', 'lon'])
my_locations = pd.concat([first_location, second_location], ignore_index=True)
print(my_locations)

# calculating the distance between Empire State Building and Marea Restaurant New Yor
p_1 = (my_locations['lat'][0], my_locations['lon'][0])
p_2 = (my_locations['lat'][1], my_locations['lon'][1]) 
d=geopy.distance.geodesic(p_1, p_2).km
print(d)
