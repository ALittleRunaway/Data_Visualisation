"""I learn how to work with json"""
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структуры данных
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # load - преобразует данные в огромный словарь, что удобно для Python

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4) # dump - об. данных json, об. файла и indent=4 (форматирование с отступами)

all_eq_dicts = all_eq_data['features'] # all_eq_dicts - это список, потому что каждое eq в features - это элемент списка
mags, lons, lats, hower_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    lons.append(lon)
    lats.append(lat)
    hower_text.append(title)
    mags.append(mag)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

# Нанесение данных на карту
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hower_text,
    'marker': {
        'size': [4*mag for mag in mags], # Будет список как mag, но где все элементы умножены на 4
        'color': mags,
        'colorscale': 'Jet',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
