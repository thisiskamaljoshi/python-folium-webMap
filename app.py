import folium
import pandas


india_map = folium.Map(
    location=[23.837415395428557, 78.73967196771261], zoom_start=5)

india_map.save("generatedIndiaMap.html")
