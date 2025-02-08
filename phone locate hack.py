import folium.map
import phonenumbers
import opencage
import folium
from opencage.geocoder import OpenCageGeocode
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
#########################################################################################################################
Inumber=phonenumbers.parse(number)
location=geocoder.description_for_number(Inumber , "en")
print(location)
b=phonenumbers.parse(number)
print(carrier.name_for_number(b),"en")
key = '12b356f613c14616bc270adf0d6170a9'
geocoder=OpenCageGeocode(key)
c=str(location)
result=geocoder.geocode(c)
# print(result)

lat = result[0]['geometry']['lat']
lan = result[0]['geometry']['lan']

print(lat , lan)
my_map=folium.map(location[lat , lan],zoom_start= 9)
folium.Marker([lat , lan] , popup=location).add_to(my_map)
my_map.save("mylocation.html")