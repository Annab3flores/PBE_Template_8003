from django.shortcuts import render

import folium
from folium.plugins import FastMarkerCluster
from core.models import EVChargingLocation

# Create your views here.
def index(request):

    stations = EVChargingLocation.objects.all()

    #create a folium map centred on Cnnecticut
    m = folium.Map(location=[41.5025,-72.699997], zoom_start=9)

    # add a marker tothe map for each station
    for station in stations:
        coordinates = (station.latitude, station.longitude)
        folium.Marker(coordinates, popup=station.station_name).add_to(m)

    # use FastMarkerCluster to generate the clusters on the map
    # to this, we pass list of all(lat, lon) tuples in the data
    
    #latitudes = [station.latitude for station in stations]
    #longitudes = [station.longitude for station in stations]

    #FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)




    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)