"""Visualising repositories"""
import requests

from plotly.graph_objs import Bar
from plotly import offline

# https://api.github.com/rate_limit - 'search'['limit']['remaining'] - число оставшихся запросов API в минуту

# Создание вызова API и сохранения ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # Объект ответа сохраняется в переменной r
print(f'Status code: {r.status_code}') # 200 - аттрибут r успешного ответа

# Обработка результатов
response_dict = r.json() # Делаем из json большой словарь
repo_dicts = response_dict['items'] # В json [] - это список со словарями-репозиториями
# repo_names, stars, labels = [], [], []
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts: # По одному репозиторию
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

# Построение визуализации
data = [{ # Влияет на вид столбцов
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'text': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred Python projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
