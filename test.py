import requests
import json

ACCESS_TOKEN = open('C:/Google Drive/other/token.txt').read()  # здесь вы указываете путь к своему токену доступа
PHOTOS_SEARCH_V = 5.107
NEWSFEED_SEARCH_V = 5.107
FRIENDS_GET_V = 5.107
GROUPS_GETMEMBERS_V = 5.107
USERS_GET_V = 5.107
GROUPS_GET_BY_ID_V = 5.107

params = {
    'access_token': ACCESS_TOKEN,
    'v': USERS_GET_V,
    'user_ids': 10
}
try:
    print(requests.get(f"https://api.vk.com/method/users.get?", params=params).json())
    print('Попытка')
except:
    print('Ошибка')
