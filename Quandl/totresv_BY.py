"""Total reserves in Belarus"""
from plotly import offline
from plotly.graph_objs import Layout
import requests

# Вызов API и сохранение ответа
url = 'https://www.quandl.com/api/v3/datasets/WGEM/BLR_TOTRESV?start_date=1994-12-31&end_date' \
      '=2018-12-31&api_key=sQxeKyf_fAKrwE_jH6Wf'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Обработка информации о каждой дате
tr_values = r.json()
values, dates = [], []
for item in tr_values['dataset']['data']:
    # values.append((format(item[1], '.2f')))
    values.append(int(item[1]))
    dates.append(item[0])

# title = tr_values['dataset']['description']
# dot = title.find('.')
# name = title[:dot]
# description = title[dot+2:]
# title = f"<b>{name}</b><br>{description[:84]}<br>{description[84:]}"

# Построение визуализации
data = [{
    'type': 'bar',
    'x': dates,
    'y': values,
    # 'text': labels,
    'marker': {
        'color': 'rgb(107 ,142, 35)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.8,
    'orientation': 'v',
}]
my_layout = {
    'title': tr_values['dataset']['name'],
    'titlefont': {'color': 'black', 'size': 28},
    'xaxis': {
        'title': tr_values['dataset']['column_names'][0],
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': tr_values['dataset']['column_names'][1],
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='totresv_Bel.html')
