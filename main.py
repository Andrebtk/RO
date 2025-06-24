import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

import paris


home = [48.845080, 2.349461]

#Create the map
my_map = folium.Map(location = home, zoom_start = 17)

folium.Marker(
    location=home,
    tooltip="Source",
    popup="Source: Home",
    icon=folium.Icon(icon="home"),
).add_to(my_map)



paris.metro(my_map)


#Display the map
my_map.save("map.html")


webbrowser.open("map.html")
