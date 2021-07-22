import folium
from folium.plugins import HeatMap
import json
import webbrowser
import os

point_data = json.loads(open('./data/point.json', mode='r', encoding='utf-8').read())

m2 = folium.Map(location=[36.505354, 127.704334], zoom_start=7, titles='Cartodb Positron')
HeatMap(point_data).add_to(m2)

m2.save('./data/heatmap.html')

webbrowser.open(os.getcwd() + '/data/heatmap.html')