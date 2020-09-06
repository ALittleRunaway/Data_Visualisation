"""I learn to work with the API"""
import requests

# https://api.github.com/rate_limit - 'search'['limit']['remaining'] - число оставшихся запросов API в минуту

# Создание вызова API и сохранения ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # Объект ответа сохраняется в переменной r
print(f'Status code: {r.status_code}') # 200 - аттрибут r успешного ответа

# Сохранение ответа API в переменной
response_dict = r.json() # Как-то делаем словарь
print(f"Total repositories: {response_dict['total_count']}")

# # Обработка результатов
# print(response_dict.keys())

# Анализ информации о репозиториях
repo_dicts = response_dict['items'] # В json [] - это список со словарями
print(f'Repositories returned: {len(repo_dicts)}')

# Анализ первого репозитория
# repo_dict = repo_dicts[0]
# print(f'\nKeys: {len(repo_dict)}')
# for key in sorted(repo_dict.keys()):
#     print(key)
print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f'\nName: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    print(f'Created: {repo_dict["created_at"]}')
    print(f'Updated: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')

