import folium

map = folium.Map(
    location = [-10.185567, -48.311290],
    titles = 'Casa do Luscca',
    zoom_start = 16
)

folium.Marker(
    [-10.185567, -48.311290],
    popup = '<i> Casa do Luscca</i>',
    tooltip = 'Clique Aqui'
).add_to(map)

map.save('C:\Users\awsod\Downloads\map.html')
