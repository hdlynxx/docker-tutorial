from geopy.geocoders import Nominatim

def where_is_kantoor():
    geolocator = Nominatim(user_agent="docker_tutorial_app")
    location = geolocator.reverse('52.1538181, 5.3703867')
    loc = location.raw
    loc_dict = location.raw
    print(loc_dict['address'])

where_is_kantoor()