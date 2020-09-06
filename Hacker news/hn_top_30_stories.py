"""Visual"""
from plotly import offline
from operator import itemgetter
import requests

# Вызов API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Обработка информации о каждой статье
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    response_dict = r.json()
    try:
        comm = response_dict["descendants"]
    except:
        comm = 0

    # Посторение словаря для каждой статьи
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
        'comments': comm
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
titles, comments = [], []
for submission_dict in submission_dicts:
    titles.append(f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>")
    comments.append(submission_dict['comments'])

# Построение визуализации
data = [{ # Влияет на вид столбцов
    'type': 'bar',
    # 'x': titles,
    # 'y': comments,
    'x': comments,
    'y': titles,
    # 'text': labels,
    'marker': {
        'color': 'rgb(255, 140, 0)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.8,
    'orientation': 'h',
}]
my_layout = {
    'title': 'Top 30 stories on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stories',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_visual.html')
