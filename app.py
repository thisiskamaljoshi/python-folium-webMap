import folium
import pandas


india_map = folium.Map(
    location=[23.837415395428557, 78.73967196771261], zoom_start=5)

cities_json = [
    {
        "location": [26.710566759401036, 80.93976796750837],
        "name":"Lucknow",
        "color":"green"
    },
    {
        "location": [28.622308156232425, 77.20612915279953],
        "name":"Delhi",
        "color":"blue"
    },
    {
        "location": [27.176933823103095, 75.81147977428485],
        "name":"Jaipur",
        "color":"orange"
    },
    {
        "location": [25.63133374990229, 85.12116611475751],
        "name":"Patna",
        "color":"darkblue"
    },
    {
        "location": [21.36653214810503, 79.51561852698572],
        "name":"Nagpur",
        "color":"purple"
    },
    {
        "location": [22.70190941163953, 72.7148172020967],
        "name":"Ahmedabad",
        "color":"lightred"
    },
    {
        "location": [27.176933823103095, 75.81147977428485],
        "name":"Jaipur",
        "color":"orange"
    },
    {
        "location": [23.322752215859836, 85.26971346662],
        "name":"Ranchi",
        "color":"green"
    },
    {
        "location": [20.494449286446347, 85.85618668360118],
        "name":"Bhubaneswar",
        "color":"red"
    },
    {
        "location": [18.34531663478403, 73.88383037057251],
        "name":"Pune",
        "color":"pink"
    },
]

# Cities
cities = folium.FeatureGroup(name="Cities")

for city in cities_json:
    cities.add_child(folium.Marker(
        location=city["location"], popup=city["name"], icon=folium.Icon(color=city["color"])))


# GeoJson

polygonLayer = folium.FeatureGroup(name="Geo Json")
polygonLayer.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

india_map.add_child(cities)
india_map.add_child(polygonLayer)
india_map.add_child(folium.LayerControl())
india_map.save("generatedIndiaMap.html")
