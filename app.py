import folium
import pandas


india_map = folium.Map(
    location=[23.837415395428557, 78.73967196771261], zoom_start=5)


# Lucknow
cities = folium.FeatureGroup(name="Cities")

cities.add_child(folium.Marker(
    location=[26.710566759401036, 80.93976796750837], popup="Lucknow", icon=folium.Icon(color="green")))


# Delhi

cities.add_child(folium.Marker(
    location=[28.622308156232425, 77.20612915279953], popup="Delhi", icon=folium.Icon(color="blue")))


# Jaipur

cities.add_child(folium.Marker(
    location=[27.176933823103095, 75.81147977428485], popup="Jaipur", icon=folium.Icon(color="orange")))


india_map.add_child(cities)
india_map.save("generatedIndiaMap.html")
