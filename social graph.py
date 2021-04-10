from pandas import DataFrame, read_excel
from requests import get
from time import sleep
import networkx as nx
from IPython.display import Image
import matplotlib.pyplot as plt

ACCESS_TOKEN = open('token.txt').read()
max_one_count = {  # максимальное количество в запросов за раз
    'newsfeed.search': 200,
    'photos.search': 1000,
    'friends.get': 10000,
    'video.search': 200,
    'groups.getMembers': 1000,
}

total_max_count = {  # максимальное количество запросов вообще
    'newsfeed.search': 1000,
    'photos.search': 3000,
    'video.search': 1000,
    'friends.get': 10000,  # больше 10000 не бывает
    'groups.getMembers': None,  # нет ограничений?
}

PHOTOS_SEARCH_V = 5.126
VIDEO_SEARCH_V = 5.126
NEWSFEED_SEARCH_V = 5.107
FRIENDS_GET_V = 5.107
GROUPS_GETMEMBERS_V = 5.107
GROUPS_GET_BY_ID_V = 5.107
USERS_GET_V = 5.126

file_to_analyze = 'test_getusers_analyze.xlsx'
data_dicts = read_excel(file_to_analyze).to_dict(orient='records')

list_id = list()  # записываем спискок с анализируемыми id
for dict in data_dicts:
    if str(dict['id']) not in list_id:
        list_id.append(str(dict['id']))

dict_to_graph = {}  # создаём словарь, где
# ключ - id пользователя из списка
# содержание - находится информация о странице

list_id_private = []  # список id с закрытыми странциами
list_id_not_private = []  # список id с открытыми странциами

# получим список друзей и другую информацию страниц
for user_id in list_id:
    request_type = 'friends.get'
    params = {'access_token': ACCESS_TOKEN,
              'user_id': user_id,
              'v': FRIENDS_GET_V}
    sleep(0.34)
    request_json = get(f"https://api.vk.com/method/{request_type}?", params=params).json()

    if 'response' in request_json:

        friends = []
        for friend in request_json['response']['items']:
            if str(friend) in list_id:
                friends.append(str(friend))

        dict_to_graph.update(
            {str(user_id):
                {
                    'is_private': False,
                    'friends': friends
                }
            }
        )
        list_id_not_private.append(str(user_id))

    else:
        dict_to_graph.update(
            {str(user_id):
                {
                    'is_private': True,
                    'friends': None
                }
            }
        )
        list_id_private.append(str(user_id))

# проанализируем все страницы и найдём упоминание приватных страниц
for private_id in list_id_private:

    friends = []
    for not_private_id in list_id_not_private:
        if private_id in dict_to_graph[not_private_id]['friends']:
            friends.append(not_private_id)

    dict_to_graph[private_id].update({'friends': friends})

for person in dict_to_graph:
    print(person, dict_to_graph[person])

social_graph = nx.Graph()
for person_id in dict_to_graph:
    social_graph.add_node(person_id)
    for friend in dict_to_graph[person_id]['friends']:
        social_graph.add_edge(person_id, friend)

pos = nx.spectral_layout(social_graph)

nx.draw(
    social_graph,
    node_color='red',
    node_size=1000,
    with_labels=True
)

plt.show()

print('Готово!')
