"""I want to build it myself"""
import requests
import json

# Вызов API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}\n')

# Анализ структуры данных
ids_list = r.json()

def idStatus(story_id):
    """Shows id status"""
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    r = requests.get(url)
    print(f'id: {story_id}\tstatus:{r.status_code}')

def getInfo(story_id):
    """Does everything"""
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    r = requests.get(url)
    response_dict = r.json()
    comms = response_dict['descendants']
    title = response_dict['title']
    link = f'https://news.ycombinator.com/item?id={story_id}'
    print(f'\nTitle: {title}\nDiscussion link: {link}\nComments: {comms}')

for story_id in ids_list[:10]:
    idStatus(story_id)

for story_id in ids_list[:10]:
    getInfo(story_id)
