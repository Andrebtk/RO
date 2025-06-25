import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

from paris import Metro
from graph import Graph

home = [48.845080, 2.349461]

#Create the map
my_map = folium.Map(location = home, zoom_start = 17)

folium.Marker(
    location=home,
    tooltip="Source",
    popup="Source: Home",
    icon=folium.Icon(icon="home"),
).add_to(my_map)


metro = Metro(my_map)

metro.plot_graph()
"""
#Display the map
my_map.save("map.html")


webbrowser.open("map.html")
"""
