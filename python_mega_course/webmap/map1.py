#%%
import folium
import pandas

#%%
data = pandas.read_csv("Volcanoes.txt")

print(data.keys())
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
elev = list(data['ELEV'])

#%%
map = folium.Map(
    location=(45.508775, -120.067313),
    zoom_start=6,
    tiles="Stamen Toner"
    )

#%%
def color(el):
    if int(el) > 4000:
        return 'red'
    elif int(el) > 2000:
        return 'orange'
    else:
        return 'green'

#%%
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")
for lt, ln, n, el in zip(lat,lon,name, elev):
    fgv.add_child(folium.CircleMarker(
                    location = (
                        lt,
                        ln),
                    popup = str(int(el))+
                        ' m',
                    tooltip = n,
                    color = color(el),
                    radius = 4,
                    weight = 7,
                    fill = True,
                    fillOpacity = 1.0
                    )
                    
                )

#%%
fgp.add_child(
    folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
                    style_function=lambda x: {'fillColor': 
                        'green' if x['properties']['POP2005'] < 10000000
                        else
                        'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                        else
                        'red'
                        }                    
                    ))


#%%
map.add_child(fgv)
map.add_child(fgp)

#%%
map.add_child(folium.LayerControl())
#%%
map.save("Map1.html")


#%%
