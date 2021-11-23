import folium

place = folium.Map(location=[42.875734, 74.611622], zoom_start=12)
folium.TileLayer('CartoDB dark_matter', 'openstreetmap').add_to(place)
#CartoDB dark_matter
folium.Marker(location=[42.875734, 74.611622],popup="Downtown", icon=folium.Icon(color='gray')).add_to(place)
folium.Marker(location=[42.844475, 74.615644],popup="Home", icon=folium.Icon(color='green')).add_to(place)
place.save("map1.html")