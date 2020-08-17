"""Hacker news API"""
import requests
import json

# Вызов API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/item/24143979.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Анализ структуры данных
response_dict = r.json() # Делаем из json большой словарь
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
