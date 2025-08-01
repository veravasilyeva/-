from opencage.geocoder import OpenCageGeocode

key = 'bae2871de12f4b3ea92b4f80fcfbb984'
city = 'Moscow'

def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"

key = 'bae2871de12f4b3ea92b4f80fcfbb984'
city = 'Moscow'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city} : {coordinates}')

query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'

# no need to URI encode query, module does that for you
results = geocoder.geocode(query)

