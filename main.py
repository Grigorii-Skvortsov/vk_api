from pandas import DataFrame, read_excel
from requests import get
from datetime import datetime
from time import sleep, mktime  # sleep(1) - заснуть на 1 секунду
from sys import argv as sys_argv, exit as sys_exit
from PyQt5 import QtWidgets
from ui_window_main import Ui_MainWindow
from ui_widget_get_users import Ui_MainWindow_Get_Users
from ui_widget_newsfeed_search import Ui_MainWindow_Newsfeed_Search
from ui_widget_photos_search import Ui_MainWindow_Photos_Search


global max_one_count, total_max_count, ACCESS_TOKEN, PHOTOS_SEARCH_V, NEWSFEED_SEARCH_V, FRIENDS_GET_V, GROUPS_GETMEMBERS_V, USERS_GET_V, GROUPS_GET_BY_ID_V, USERS_GET_V

# open('C:/Google Drive/program/matirials_for_vk_api/token.txt').read() здесь вы указываете путь к своему токену доступа
ACCESS_TOKEN = open('C:/Google Drive/program/matirials_for_vk_api/token.txt').read()

max_one_count = {  # максимальное количество в запросов за раз
    'newsfeed.search': 200,
    'photos.search': 1000,
    'friends.get': 10000,
    'groups.getMembers': 1000,
}

total_max_count = {  # максимальное количество запросов вообще
    'newsfeed.search': 1000,
    'photos.search': 3000,
    'friends.get': 10000,  # больше 10000 не бывает
    'groups.getMembers': None,  # нет ограничений?
}

PHOTOS_SEARCH_V = 5.126
NEWSFEED_SEARCH_V = 5.107
FRIENDS_GET_V = 5.107
GROUPS_GETMEMBERS_V = 5.107
USERS_GET_V = 5.107
GROUPS_GET_BY_ID_V = 5.107
USERS_GET_V = 5.126

def WidgetUsersGet_show(): WidgetUsersGet.show()


def WidgetNewsfeedSearch_show(): WidgetNewsfeedSearch.show()


def WidgetPhotosSearch_show(): WidgetPhotosSearch.show()


def push_button_get_users_load():
    params = {'access_token': ACCESS_TOKEN}
    id = users_get.lineEdit_get_users_id.text()

    if id != '' and users_get.radioButton_user.isChecked():
        user_id = int(id)
        params.update({'user_id': user_id})
        params.update({'v': FRIENDS_GET_V})
        params.update({'fields': 'city, country'})
        users_get.lineEdit_get_users_status.setText('Данные выгружены')

        push_button_something_load('friends.get', params)

    elif id != '' and users_get.radioButton_group.isChecked():

        group_id = int(id)
        params.update({'group_id': group_id})
        params.update({'v': GROUPS_GETMEMBERS_V})
        params.update({'fields': 'city, country'})
        users_get.lineEdit_get_users_status.setText('Данные выгружены')

        push_button_something_load('groups.getMembers', params)

    else:
        users_get.lineEdit_get_users_status.setText('Ошибка запроса')
        if users_get.radioButton_group.isChecked():
            main_menu.textBrowser.append('Для поиска по группам необходимо указать ID группы')
        if users_get.radioButton_user.isChecked():
            main_menu.textBrowser.append('Для поиска по друзьям необходимо указать ID пользователя')


def push_button_photos_search_load():
    params = {'access_token': ACCESS_TOKEN}
    q = photos_search.lineEdit_photos_search_q.text()
    latitude = photos_search.lineEdit_photos_search_lat.text()
    longitude = photos_search.lineEdit_photos_search_long.text()
    if q != '' or (latitude != '' and longitude != ''):  # в запросе обязательно должен быть текст или координаты
        q = str(q)
        params.update({'q': q})
        params.update({'offset': 0})  # изначальное смещение относительно первого результата
        params.update({'v': PHOTOS_SEARCH_V})

        latitude = photos_search.lineEdit_photos_search_lat.text()
        longitude = photos_search.lineEdit_photos_search_long.text()
        if latitude != '' and longitude != '':
            latitude = float(latitude)
            longitude = float(longitude)
            params.update({'lat': latitude})  # северная широта
            params.update({'long': longitude})  # восточная долгота

        radius = photos_search.lineEdit_photos_search_radius.text()
        if radius != '':
            radius = int(radius)
            params.update({'radius': radius})

        start_time_day = photos_search.lineEdit_photos_search_start_time_day.text()
        start_time_month = photos_search.lineEdit_photos_search_start_time_month.text()
        start_time_year = photos_search.lineEdit_photos_search_start_time_year.text()
        if start_time_day != '' and start_time_month != '' and start_time_year != '':
            start_time_day = int(start_time_day)
            start_time_month = int(start_time_month)
            start_time_year = int(start_time_year)
            start_time = y_m_d_to_unix(start_time_year, start_time_month, start_time_day)
            params.update({'start_time': start_time})

        end_time_day = photos_search.lineEdit_photos_search_end_time_day.text()
        end_time_month = photos_search.lineEdit_photos_search_end_time_month.text()
        end_time_year = photos_search.lineEdit_photos_search_end_time_year.text()
        if end_time_day != '' and end_time_month != '' and end_time_year != '':
            end_time_day = int(end_time_day)
            end_time_month = int(end_time_month)
            end_time_year = int(end_time_year)
            end_time = y_m_d_to_unix(end_time_year, end_time_month, end_time_day)
            params.update({'end_time': end_time})

        photos_search.lineEdit_photos_search_status.setText('Данные выгружены')

        push_button_something_load('photos.search', params)
    else:
        photos_search.lineEdit_photos_search_status.setText('Ошибка запроса')
        main_menu.textBrowser.append('Для поиска по фото необходимо указать текст запроса или координаты')


def push_button_newsfeed_search_load():
    params = {'access_token': ACCESS_TOKEN}
    q = newsfeed_search.lineEdit_newsfeed_search_q.text()
    if q != '':  # в запросе обязательно должен быть текст
        q = str(q)
        params.update({'q': q})
        params.update({'v': NEWSFEED_SEARCH_V})
        params.update({'extended': 0})  # 1, если необходимо получить информацию о пользователе или сообществе

        latitude = newsfeed_search.lineEdit_newsfeed_search_latitude.text()
        longitude = newsfeed_search.lineEdit_newsfeed_search_longitude.text()
        if latitude != '' and longitude != '':
            latitude = float(latitude)
            longitude = float(longitude)
            params.update({'latitude': latitude})  # северная широта
            params.update({'longitude': longitude})  # восточная долгота

        start_time_day = newsfeed_search.lineEdit_newsfeed_search_start_time_day.text()
        start_time_month = newsfeed_search.lineEdit_newsfeed_search_start_time_month.text()
        start_time_year = newsfeed_search.lineEdit_newsfeed_search_start_time_year.text()
        if start_time_day != '' and start_time_month != '' and start_time_year != '':
            start_time_day = int(start_time_day)
            start_time_month = int(start_time_month)
            start_time_year = int(start_time_year)
            start_time = y_m_d_to_unix(start_time_year, start_time_month, start_time_day)
            params.update({'start_time': start_time})

        end_time_day = newsfeed_search.lineEdit_newsfeed_search_end_time_day.text()
        end_time_month = newsfeed_search.lineEdit_newsfeed_search_end_time_month.text()
        end_time_year = newsfeed_search.lineEdit_newsfeed_search_end_time_year.text()
        if end_time_day != '' and end_time_month != '' and end_time_year != '':
            end_time_day = int(end_time_day)
            end_time_month = int(end_time_month)
            end_time_year = int(end_time_year)
            end_time = y_m_d_to_unix(end_time_year, end_time_month, end_time_day)
            params.update({'end_time': end_time})

        newsfeed_search.lineEdit_newsfeed_search_status.setText('Данные выгружены')
        push_button_something_load('newsfeed.search', params)
    else:
        newsfeed_search.lineEdit_newsfeed_search_status.setText('Ошибка запроса')
        main_menu.textBrowser.append('Для поиска по постам необходимо указать текст запроса')


def push_button_something_load(request_type: str, params: dict):
    """i - widget number
    request_type - type of search"""
    line_inspector()
    global data
    data = []
    params.update({'access_token': ACCESS_TOKEN})  # создадим словарь, который будет содержать параметры запросы

    # сформируем сам запрос
    # ответ имеет параметр "count", по которому можно определить количество резльтатов вообще,
    # и на основании этого и total_max_count (потолка по API) нужно выбрать "count" и локальный потолок
    params.update({'count': 1})  # сделаем тестовый запрос на 1
    # сколько вообще необходимо получить?
    sleep(0.34)
    try:
        one_request = get(f"https://api.vk.com/method/{request_type}?", params=params).json()
    except:
        main_menu.textBrowser.append(
            f"Тестовый запрос '{request_type}' вернул ошибку.\n"
            f"Это может быть по следующим причинам:\n"
            f"1. Отсутсвует подсоединение к сети;\n"
            f"2. Истёк ключ доступа - обратитесь к разработчику;\n"
            f"3. Изменились настройки VK API - обратитесь к разработчику;\n"
            f"4. Неправильное заполнение формы - проверьте верность форматов заполнения.\n"
        )
        return None

    main_menu.textBrowser.append(f"Найдено {one_request['response']['count']} результатов '{request_type}'")
    # выбираем, какой взять верхний предел. Ограничение API или ограничение результатов
    this_total_max_count = one_request['response']['count'] if (total_max_count[request_type] is None) or (
            one_request['response']['count'] <= total_max_count[request_type]) else total_max_count[
        request_type]
    main_menu.textBrowser.append(
        f"С учётом глобального ограничения запросов будет загружено {this_total_max_count} результатов '{request_type}'")
    # один запрос равен "потолку API", если колчиство доступных результатов больше потолка API,
    # а если доступных результатов меньше потолка API, то равен количеству доступных результатов
    count = max_one_count[request_type] if this_total_max_count >= max_one_count[
        request_type] else this_total_max_count
    params.update({'count': count})

    offset = 0  # первый сдвиг равен 0, далее он будет расти на размер запроса

    # откроем черный список для фильтрации
    try:
        black_list = set(open('black_list.csv', 'r').read().split('\n'))
    except:
        main_menu.textBrowser.append(
            "Фильрация ID не была совершена. 'black_list.csv' не найден, "
            "создайте файл 'black_list.csv' в той же директории, что и Palantir.exe. ")
        black_list = set()

    while this_total_max_count > 0:
        sleep(0.34)
        try:
            request_json = get(f"https://api.vk.com/method/{request_type}?", params=params).json()
        except:
            main_menu.textBrowser.append(
                f"В процессе цикла запросов '{request_type}' возникла ошибка.\n"
                f"Это может быть по следующим причинам:\n"
                f"1. Нестабильное подсоединение к сети;\n"
                f"2. Истёк ключ доступа - обратитесь к разработчику;\n"
                f"3. Изменились настройки VK API - обратитесь к разработчику;\n"
                f"4. Неправильное заполнение формы - проверьте верность форматов заполнения.\n"
            )
            return None
        offset = offset + count
        if request_type == 'newsfeed.search':
            params.update({'start_from': offset})
        else:
            params.update({'offset': offset})
        main_menu.textBrowser.append(f"Осталось загрузить {this_total_max_count} результатов")
        this_total_max_count = this_total_max_count - count

        # записываем данные в переменную
        if request_type == 'newsfeed.search':
            for item in request_json['response']['items']:
                # какие параметры могут отсутствовать?
                this_id = str(item['owner_id']).replace('-', '')
                if this_id in black_list:
                    continue
                this_lat = ''
                this_long = ''
                this_place = ''
                if item.get("geo") and item["geo"].get("coordinates"):
                    if item["geo"].get("coordinates"):
                        this_lat = item["geo"]["coordinates"].split()[0]
                        this_long = item["geo"]["coordinates"].split()[1]
                    if item["geo"].get("place") and item["geo"]["place"].get("title"):
                        this_place = item["geo"]["place"]["title"]

                post_source = ' '
                for key in item["post_source"]:
                    if type(item["post_source"][key]) == str:
                        post_source += ' ' + item["post_source"][key]
                    if type(item["post_source"][key]) == dict:
                        for sub_key in item["post_source"][key]:
                            post_source += ' ' + item["post_source"][key][sub_key]

                data.append(
                    {'id': this_id,
                     'link': '=HYPERLINK("{}", "{}")'.format(
                         f"https://vk.com/id{str(item['owner_id']).replace('-', '')}", 'page link'),
                     'first_name': '',
                     'last_name': '',
                     'content': '',
                     'date': unix_to_d_m_y_str(item['date']),
                     'lat': this_lat,
                     'long': this_long,
                     'place': this_place,
                     'post_source': post_source,
                     'comments': item["comments"]["count"],
                     'likes': item["likes"]["count"],
                     'reposts': item["reposts"]["count"],
                     'text': item['text']
                     })

        elif request_type == 'photos.search':
            for item in request_json['response']['items']:
                # какие параметры могут отсутствовать?
                this_id = str(item['owner_id']).replace('-', '')
                if this_id in black_list:
                    continue
                this_lat = ''
                this_long = ''
                if item.get("lat"):
                    this_lat = item["lat"]
                    this_long = item["long"]
                data.append(
                    {'id': this_id,
                     'link': '=HYPERLINK("{}", "{}")'.format(
                         f"https://vk.com/id{str(item['owner_id']).replace('-', '')}", 'page link'),
                     'first_name': '',
                     'last_name': '',
                     'content': '=HYPERLINK("{}", "{}")'.format(str(item['sizes'][-1]['url']), 'photo link'),
                     'date': unix_to_d_m_y_str(item['date']),
                     'lat': this_lat,
                     'long': this_long,
                     'text': item['text']
                     })

        elif request_type == 'friends.get' or request_type == 'groups.getMembers':
            for item in request_json['response']['items']:
                this_id = str(item['id']).replace('-', '')
                if this_id in black_list:
                    continue
                this_country = ''
                this_city = ''
                if item.get("country"):
                    this_country = item['country']['title']
                    if item.get("city"):
                        this_city = item['city']['title']
                data.append(
                    {'id': this_id,
                     'link': '=HYPERLINK("{}", "{}")'.format(
                         f"https://vk.com/id{str(item['id']).replace('-', '')}", 'page link'),
                     'first_name': item['first_name'],
                     'last_name': item['last_name'],
                     'country': this_country,
                     'city': this_city,
                     })

    main_menu.textBrowser.append(f"{len(data)} результатов поиска загружено. Сохранить?")


def push_button_newsfeed_search_clear():
    line_inspector()
    newsfeed_search.lineEdit_newsfeed_search_status.setText('Данных нет')
    clearing_lines = [
        newsfeed_search.lineEdit_newsfeed_search_q,

        newsfeed_search.lineEdit_newsfeed_search_latitude,
        newsfeed_search.lineEdit_newsfeed_search_longitude,

        newsfeed_search.lineEdit_newsfeed_search_start_time_day,
        newsfeed_search.lineEdit_newsfeed_search_start_time_month,
        newsfeed_search.lineEdit_newsfeed_search_start_time_year,

        newsfeed_search.lineEdit_newsfeed_search_end_time_day,
        newsfeed_search.lineEdit_newsfeed_search_end_time_month,
        newsfeed_search.lineEdit_newsfeed_search_end_time_year,
    ]
    data = []
    for line in clearing_lines:
        line.clear()


def push_button_photos_search_clear():
    line_inspector()
    photos_search.lineEdit_photos_search_status.setText('Данных нет')
    clearing_lines = [
        photos_search.lineEdit_photos_search_q,

        photos_search.lineEdit_photos_search_lat,
        photos_search.lineEdit_photos_search_long,
        photos_search.lineEdit_photos_search_radius,

        photos_search.lineEdit_photos_search_start_time_day,
        photos_search.lineEdit_photos_search_start_time_month,
        photos_search.lineEdit_photos_search_start_time_year,

        photos_search.lineEdit_photos_search_end_time_day,
        photos_search.lineEdit_photos_search_end_time_month,
        photos_search.lineEdit_photos_search_end_time_year,
    ]
    data = []
    for line in clearing_lines:
        line.clear()


def push_button_get_users_clear():
    line_inspector()
    users_get.lineEdit_get_users_status.setText('Данных нет')
    clearing_lines = [
        users_get.lineEdit_get_users_id,
    ]
    data = []
    for line in clearing_lines:
        line.clear()


def push_button_get_users_save(): push_button_something_save('get.users')


def push_button_photos_search_save(): push_button_something_save('photos.search')


def push_button_newsfeed_search_save(): push_button_something_save('newsfeed.search')


def push_button_something_save(window_type: str):
    """i - widget number
    window_type - type of window"""
    line_inspector()
    status_line = {
        'newsfeed.search': newsfeed_search.lineEdit_newsfeed_search_status,
        'photos.search': photos_search.lineEdit_photos_search_status,
        'get.users': users_get.lineEdit_get_users_status,
    }

    if len(data) > 0:
        file_name = {
            'newsfeed.search': newsfeed_search.lineEdit_newsfeed_search_file_name.text(),
            'photos.search': photos_search.lineEdit_photos_search_file_name.text(),
            'get.users': users_get.lineEdit_get_users_file_name.text(),
        }

        this_name = f"{file_name[window_type]}_{window_type.replace('.', '')}.xlsx"
        try:
            data_frame = DataFrame.from_dict(data)  # преобразовываем в data frame
            data_frame.to_excel(this_name, index=False)  # перезаписываем файл в excel

            status_line[window_type].setText('Записано в файл')
            main_menu.textBrowser.append(f"В файл '{this_name}' сохранено {len(data)} id")
        except:
            status_line[window_type].setText('Ошибка!')
            main_menu.textBrowser.append(f"При сохранении файла '{this_name}' произошла ошибка!\n"
                                         f"- Файл не должен быть открыт во время сохранения\n"
                                         f"- Работа гарантирована на современных версиях Windows")
    else:
        pass


def push_button_get_group_id():
    line_inspector()
    if main_menu.lineEdit_get_group_id_txt_id.text() != '':
        params = {
            'access_token': ACCESS_TOKEN,
            'v': GROUPS_GET_BY_ID_V,
            'group_ids': main_menu.lineEdit_get_group_id_txt_id.text()
        }
        sleep(0.34)
        try:
            main_menu.lineEdit_get_group_id_id.setText(str(get(f"https://api.vk.com/method/groups.getById?",
                                                               params=params).json()['response'][0]['id']))
        except:
            main_menu.textBrowser.append(
                f"Запрос получеия ID группы '{params['group_ids']}' вернул ошибку.\n"
                f"Это может быть по следующим причинам:\n"
                f"1. Отсутсвует подсоединение к сети;\n"
                f"2. Истёк ключ доступа - обратитесь к разработчику;\n"
                f"3. Изменились настройки VK API - обратитесь к разработчику;\n"
                f"4. Неправильное заполнение формы - проверьте верность форматов заполнения.\n"
            )
            return None


def push_button_get_user_id():
    line_inspector()
    if main_menu.lineEdit_get_user_id_txt_id.text() != '':
        params = {
            'access_token': ACCESS_TOKEN,
            'v': USERS_GET_V,
            'user_ids': main_menu.lineEdit_get_user_id_txt_id.text()
        }
        sleep(0.34)
        try:
            main_menu.lineEdit_get_user_id_id.setText(str(get(f"https://api.vk.com/method/users.get?",
                                                              params=params).json()['response'][0]['id']))
        except:
            main_menu.textBrowser.append(
                f"Запрос получеия ID пользователя '{params['user_ids']}' вернул ошибку.\n"
                f"Это может быть по следующим причинам:\n"
                f"1. Отсутсвует подсоединение к сети;\n"
                f"2. Истёк ключ доступа - обратитесь к разработчику;\n"
                f"3. Изменились настройки VK API - обратитесь к разработчику;\n"
                f"4. Неправильное заполнение формы - проверьте верность форматов заполнения.\n"
            )
            return None


def push_button_user_file_analyze():
    params = {'access_token': ACCESS_TOKEN,
              'v': USERS_GET_V}

    file_to_analyze = f'{main_menu.lineEdit_user_file_analyze.text().replace(".xlsx", "")}.xlsx'

    data_dicts = read_excel(file_to_analyze).to_dict(orient='records')


    id_set = set()
    for dict in data_dicts:
        id_set.add(str(dict['id']))

    lists_id = []
    list_id = []
    counter = 0
    for id in id_set:
        counter += 1
        list_id.append(id)
        if counter == 100:
            counter = 0
            lists_id.append(list_id)
            list_id = []
    if len(list_id) != 0:
        lists_id.append(list_id)
        list_id = []
    data_dicts = []

    for user_ids in lists_id:
        params.update({
            'user_ids': ' ,'.join(user_ids),
            'fields': 'maiden_name, nickname, sex, bdate, city, country, connections, contacts, site',
        })
        sleep(0.34)
        print('Запрос!')
        response = get("https://api.vk.com/method/users.get?", params=params).json()

        for user in response['response']:

            data_dicts.append({
                "id": user["id"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "nickname": user["nickname"] if "nickname" in user else '',
                "maiden_name": user["maiden_name"] if "maiden_name" in user else '',
                "is_closed": int(user["is_closed"]) if "is_closed" in user else '',

                "sex": user["sex"] if "sex" in user else '',

                "bdate": user["bdate"] if "bdate" in user else '',

                "city": user["city"]["title"] if "city" in user and "title" in user["city"] else '',
                "country": user["country"]["title"] if "country" in user and "title" in user["country"] else '',

                "facebook": user["facebook"] if "facebook" in user else '',
                "facebook_name": user["facebook_name"] if "facebook_name" in user else '',
                "twitter": user["twitter"] if "twitter" in user else '',
                "instagram": user["instagram"] if "instagram" in user else '',
                "skype": user["skype"] if "skype" in user else '',
                "livejournal": user["livejournal"] if "livejournal" in user else '',

                "mobile_phone": user["mobile_phone"] if "mobile_phone" in user else '',
                "home_phone": user["home_phone"] if "home_phone" in user else '',

                "site": user["site"] if "site" in user else '',
            })

    data_frame = DataFrame.from_dict(data_dicts)  # преобразовываем в data frame

    this_name = f'{file_to_analyze.replace(".xlsx", "")}_analyze.xlsx'
    data_frame.to_excel(this_name, index=False)  # перезаписываем файл в excel
    main_menu.textBrowser.append(f"В файл '{this_name}' сохранено {len(data_dicts)} записей")


def push_button_find_intersections_search():
    line_inspector()
    pass
    first_file_name = main_menu.lineEdit_find_intersections_file_1.text()
    second_file_name = main_menu.lineEdit_find_intersections_file_2.text()
    if first_file_name != '' and second_file_name != '':
        try:
            with open(first_file_name) as first_file:
                first_set = set()
                for line in first_file:
                    first_set.add(line[0:-2])
        except:
            main_menu.textBrowser.append(
                f"Файл '{first_file_name}' отсутсвует в директории программы или имеет неподходящий формат.\n"
                f"Поиск пересечений не выполнен.\n")
            return None
        try:
            with open(second_file_name) as second_file:
                second_set = set()
                for line in second_file:
                    second_set.add(line[0:-2])
        except:
            main_menu.textBrowser.append(
                f"Файл '{second_file_name}' отсутсвует в директории программы или имеет неподходящий формат.\n"
                f"Поиск пересечений не выполнен.\n")
            return None
        this_black_list = set()
        try:
            with open('black_list.csv', 'r') as black_list_file:
                for item in black_list_file:
                    ignor_item = item.replace('\n', '')
                    this_black_list.add(ignor_item)
        except:
            main_menu.textBrowser.append(
                f"Файл игнорируемых ID 'black_list.csv' отсутсвует в директории программы"
                f" или имеет неподходящий формат. Поиск пересечений прошёл без фильтрации по чёрному списку.\n")
        global intersection_set
        intersection_set = (first_set & second_set) - this_black_list
        main_menu.textBrowser.append(f"В '{first_file_name}' и '{second_file_name}' найдено {len(intersection_set)} "
                                     f"пересечений.\n")

        main_menu.lineEdit_find_intersections_status.setText('Отфильтрованно')
    else:
        main_menu.textBrowser.append(f"Впишите в поля полные имена csv-файлов для фильтрации, например 'test.csv'.\n")
        main_menu.lineEdit_find_intersections_status.setText('Укажите файлы!')


def push_button_find_intersections_save():
    pass
    push_button_find_intersections_search()
    global intersection_set
    if intersection_set:
        this_name = f"{main_menu.lineEdit_file_name.text()}_intersections.csv"
        with open(this_name, 'w') as file:
            for id in intersection_set:
                file.write(str(id).replace('-', '') + '\n')
        main_menu.textBrowser.append(f"{len(intersection_set)} id сохранено в '{this_name}'")
    else:
        main_menu.textBrowser.append(f"Впишите в поля полные имена csv-файлов для фильтрации, например 'test.csv'.\n")
        main_menu.lineEdit_find_intersections_status.setText('Нет данных!')


def push_button_find_intersections_clear():
    line_inspector()
    main_menu.lineEdit_find_intersections_file_1.clear()
    main_menu.lineEdit_find_intersections_file_2.clear()
    global intersection_set
    intersection_set = set()


def push_button_integration_find():
    line_inspector()
    pass
    first_file_name = main_menu.lineEdit_integration_file_1.text()
    second_file_name = main_menu.lineEdit_integration_file_2.text()
    if first_file_name != '' and second_file_name != '':
        try:
            with open(first_file_name) as first_file:
                first_set = set()
                for line in first_file:
                    first_set.add(line[0:-2])
        except:
            main_menu.textBrowser.append(
                f"Файл '{first_file_name}' отсутсвует в директории программы или имеет неподходящий формат.\n"
                f"Объединение не выполнено.\n")
            return None
        try:
            with open(second_file_name) as second_file:
                second_set = set()
                for line in second_file:
                    second_set.add(line[0:-2])
        except:
            main_menu.textBrowser.append(
                f"Файл '{second_file_name}' отсутсвует в директории программы или имеет неподходящий формат.\n"
                f"Объединение не выполнено.\n")
            return None
        this_black_list = set()
        try:
            with open('black_list.csv', 'r') as black_list_file:
                for item in black_list_file:
                    ignor_item = item.replace('\n', '')
                    this_black_list.add(ignor_item)
        except:
            main_menu.textBrowser.append(
                f"Файл игнорируемых ID 'black_list.csv' отсутсвует в директории программы"
                f" или имеет неподходящий формат. Объединение прошло без фильтрации по чёрному списку.\n")
        global integration_set
        integration_set = first_set.union(second_set) - this_black_list
        main_menu.textBrowser.append(f"Файлы '{first_file_name}' и '{second_file_name}' объединены во множество "
                                     f"длинной {len(integration_set)} элементов.\n")

        main_menu.lineEdit_integration_status.setText('Объединено')
    else:
        main_menu.textBrowser.append(f"Впишите в поля полные имена csv-файлов для объединения, например 'test.csv'.\n")
        main_menu.lineEdit_integration_status.setText('Укажите файлы!')


def push_button_integration_save():
    push_button_integration_find()
    pass
    global integration_set
    if integration_set:
        this_name = f"{main_menu.lineEdit_integration_file_name.text()}_integration.csv"
        with open(this_name, 'w') as file:
            for id in integration_set:
                file.write(str(id).replace('-', '') + '\n')
        main_menu.textBrowser.append(f"{len(integration_set)} id сохранено в '{this_name}'")
    else:
        main_menu.textBrowser.append(f"Впишите в поля полные имена csv-файлов для объединения, например 'test.csv'.\n")
        main_menu.lineEdit_integration_status.setText('Нет данных!')


def push_button_integration_clear():
    line_inspector()
    main_menu.lineEdit_integration_file_1.clear()
    main_menu.lineEdit_integration_file_2.clear()
    global integration_set
    integration_set = set()


def push_button_black_list_add():
    line_inspector()
    ignored_object = main_menu.lineEdit_black_list_object.text()
    try:
        if ignored_object != '':
            with open('black_list.csv', 'r') as old_black_list_file:
                if (ignored_object + '\n') not in old_black_list_file:
                    with open('black_list.csv', 'r') as old_black_list_file:
                        new_black_list = set()
                        new_black_list.add(ignored_object + '\n')
                        for item in old_black_list_file:
                            new_black_list.add(item)
                    with open('black_list.csv', 'w') as new_black_list_file:
                        for writing_item in new_black_list:
                            new_black_list_file.write(writing_item)
                        main_menu.textBrowser.append(f"{ignored_object} добавлен в 'black_list.csv'")
                else:
                    main_menu.textBrowser.append(f"'black_list.csv' уже содержит в себе {ignored_object}")
        else:
            main_menu.textBrowser.append(f"Впишите, что вы хотите добавить в 'black_list.csv'")
    except:
        main_menu.textBrowser.append("'black_list.csv' не найден, создайте файл 'black_list.csv' в той же директории,"
                                     "что и Palantir.exe")


def push_button_black_list_seize():
    line_inspector()
    disignored_object = main_menu.lineEdit_black_list_object.text()
    try:
        if disignored_object != '':
            with open('black_list.csv', 'r') as old_black_list_file:
                if (disignored_object + '\n') in old_black_list_file:
                    with open('black_list.csv', 'r') as old_black_list_file:
                        new_black_list = set()
                        for item in old_black_list_file:
                            if item.replace('\n', '') != '\n' and item.replace('\n', '') != disignored_object:
                                new_black_list.add(item)
                    with open('black_list.csv', 'w') as new_black_list_file:
                        for writing_item in new_black_list:
                            new_black_list_file.write(writing_item)
                    main_menu.textBrowser.append(f"{disignored_object} изъят из 'black_list.csv'")
                else:
                    main_menu.textBrowser.append(f"'black_list.csv' не содержит в себе {disignored_object}")
        else:
            main_menu.textBrowser.append(f"Впишите, что вы хотите изъять из 'black_list.csv'")
    except:
        main_menu.textBrowser.append("'black_list.csv' не найден, создайте файл 'black_list.csv' в той же директории,"
                                     "что и Palantir.exe")


def push_button_black_list_display():
    line_inspector()
    try:
        with open('black_list.csv', 'r') as file:
            what_len = set()
            for item in file:
                what_len.add(item)
        main_menu.textBrowser.append(f"'black_list.csv' содержит {len(what_len)} элементов:")
        with open('black_list.csv', 'r') as file:
            for item in file:
                main_menu.textBrowser.append(item.replace('\n', ''))
    except:
        main_menu.textBrowser.append("'black_list.csv' не найден, создайте файл 'black_list.csv' в той же директории,"
                                     "что и Palantir.exe")


def line_inspector():
    """Функция инспектирует на правильность заполнения полей ввода"""
    # список полей, где могут быть только целые числа
    only_integro_lines_list = [
        main_menu.lineEdit_black_list_object,
        main_menu.lineEdit_get_group_id_id,
        main_menu.lineEdit_get_user_id_id,

        newsfeed_search.lineEdit_newsfeed_search_start_time_day,
        newsfeed_search.lineEdit_newsfeed_search_start_time_month,
        newsfeed_search.lineEdit_newsfeed_search_start_time_year,
        newsfeed_search.lineEdit_newsfeed_search_end_time_day,
        newsfeed_search.lineEdit_newsfeed_search_end_time_month,
        newsfeed_search.lineEdit_newsfeed_search_end_time_year,

        photos_search.lineEdit_photos_search_radius,
        photos_search.lineEdit_photos_search_end_time_day,
        photos_search.lineEdit_photos_search_end_time_month,
        photos_search.lineEdit_photos_search_end_time_year,
        photos_search.lineEdit_photos_search_start_time_day,
        photos_search.lineEdit_photos_search_start_time_month,
        photos_search.lineEdit_photos_search_start_time_year,

    ]

    # список полей, где число может быть десятичным (например - координаты)
    maybe_float_lines_list = [
        newsfeed_search.lineEdit_newsfeed_search_latitude,
        newsfeed_search.lineEdit_newsfeed_search_longitude,

        photos_search.lineEdit_photos_search_lat,
        photos_search.lineEdit_photos_search_long,
    ]

    # список полей, где не должно быть пробелов
    text_lines_without_spaces = [
        main_menu.lineEdit_get_group_id_txt_id,
        main_menu.lineEdit_get_user_id_txt_id,

        main_menu.lineEdit_find_intersections_file_1,
        main_menu.lineEdit_find_intersections_file_2,
        main_menu.lineEdit_file_name,

        main_menu.lineEdit_integration_file_1,
        main_menu.lineEdit_integration_file_2,
        main_menu.lineEdit_integration_file_name,

        newsfeed_search.lineEdit_newsfeed_search_file_name,

        photos_search.lineEdit_photos_search_file_name,

        users_get.lineEdit_get_users_id,
        users_get.lineEdit_get_users_file_name,
    ]

    # список полей, где может быть только текст (удалятся пробелы)
    text_lines_list = [
        newsfeed_search.lineEdit_newsfeed_search_q,
        photos_search.lineEdit_photos_search_q,
    ]

    for line in only_integro_lines_list:
        fixed_line = line.text().replace(' ', '').replace(',', '.')  # исправляем те ошибки, что можем
        if fixed_line.count('.') <= 1 and fixed_line.replace('.', ' ').isdigit():
            new_value = int(fixed_line)
            line.setText(str(new_value))
        elif fixed_line == '':
            line.setText(str(fixed_line))
        else:  # чистим поля, если там не числа и не пустота
            line.clear()

    for line in maybe_float_lines_list:
        fixed_line = line.text().replace(' ', '').replace(',', '.')  # исправляем те ошибки, что можем
        if fixed_line.count('.') <= 1 and fixed_line.replace('.', '').isdigit():
            fixed_line = str(float(fixed_line))
            line.setText(fixed_line)
        else:  # чистим поля, если там не числа и не пустота
            line.clear()

    for line in text_lines_without_spaces:
        line.setText(line.text().replace(' ', ''))

    for line in text_lines_list:
        fixed_line = line.text().replace(' ', '')
        if fixed_line == '':
            line.clear()


def unix_to_d_m_y_str(unix: int) -> str:
    """Функция получет на вход время в unix-формате, возвращает словарь с годом, месяцем и днём"""
    return f"{datetime.fromtimestamp(unix).strftime('%d')}.{datetime.fromtimestamp(unix).strftime('%m')}.{datetime.fromtimestamp(unix).strftime('%Y')[2:]} "


def y_m_d_to_unix(y: int, m: int, d: int) -> str:
    """Функция получет на вход дату (год, месяц и день) возвращает дату в unix-формате"""
    time_tuple = (y, m, d, 0, 0, 0, 0, 0, 0)
    return repr(mktime(time_tuple))


def main():
    global main_menu, data, \
        users_get, WidgetUsersGet, \
        newsfeed_search, WidgetNewsfeedSearch, \
        photos_search, WidgetPhotosSearch

    data = []
    app = QtWidgets.QApplication(sys_argv)  # Create application - инициализация приложения

    main_menu = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню
    main_menu.setupUi(MainWindow)

    MainWindow.show()

    main_menu.pushButton_get_group_id.clicked.connect(push_button_get_group_id)
    main_menu.pushButton_get_user_id.clicked.connect(push_button_get_user_id)

    main_menu.pushButton_find_intersections_search.clicked.connect(push_button_find_intersections_search)
    main_menu.pushButton_find_intersections_clear.clicked.connect(push_button_find_intersections_clear)
    main_menu.pushButton_find_intersections_save.clicked.connect(push_button_find_intersections_save)

    main_menu.pushButton_integration_find.clicked.connect(push_button_integration_find)
    main_menu.pushButton_integration_clear.clicked.connect(push_button_integration_clear)
    main_menu.pushButton_integration_save.clicked.connect(push_button_integration_save)

    main_menu.pushButton_black_list_add.clicked.connect(push_button_black_list_add)
    main_menu.pushButton_black_list_seize.clicked.connect(push_button_black_list_seize)
    main_menu.pushButton_black_list_display.clicked.connect(push_button_black_list_display)

    main_menu.pushButton_user_file_analyze.clicked.connect(push_button_user_file_analyze)

    # инициация окна получения ID подписчиков страниц и групп, привязка функций к кнопкам
    users_get = Ui_MainWindow_Get_Users()
    WidgetUsersGet = QtWidgets.QMainWindow()
    users_get.setupUi(WidgetUsersGet)

    main_menu.pushButton_get_users.clicked.connect(WidgetUsersGet_show)
    users_get.pushButton_get_users_clear.clicked.connect(push_button_get_users_clear)
    users_get.pushButton_get_users_save.clicked.connect(push_button_get_users_save)
    users_get.pushButton_get_users_load.clicked.connect(push_button_get_users_load)

    # инициация окна поиска постов, привязка функций к кнопкам
    newsfeed_search = Ui_MainWindow_Newsfeed_Search()
    WidgetNewsfeedSearch = QtWidgets.QMainWindow()
    newsfeed_search.setupUi(WidgetNewsfeedSearch)

    main_menu.pushButton_newsfeed_search.clicked.connect(WidgetNewsfeedSearch_show)
    newsfeed_search.pushButton_newsfeed_search_clear.clicked.connect(push_button_newsfeed_search_clear)
    newsfeed_search.pushButton_newsfeed_search_save.clicked.connect(push_button_newsfeed_search_save)
    newsfeed_search.pushButton_newsfeed_search_load.clicked.connect(push_button_newsfeed_search_load)

    # инициация окна поиска фото, привязка функций к кнопкам
    photos_search = Ui_MainWindow_Photos_Search()
    WidgetPhotosSearch = QtWidgets.QMainWindow()
    photos_search.setupUi(WidgetPhotosSearch)

    main_menu.pushButton_photos_search.clicked.connect(WidgetPhotosSearch_show)
    photos_search.pushButton_photos_search_clear.clicked.connect(push_button_photos_search_clear)
    photos_search.pushButton_photos_search_save.clicked.connect(push_button_photos_search_save)
    photos_search.pushButton_photos_search_load.clicked.connect(push_button_photos_search_load)

    main_menu.textBrowser.append('Программа "Bigl" ("Бигль") готова к использованию\n'
                                 'Версия - Alpha 0.5\n'
                                 'Связь с автором - GregoryValeryS@gmail.com\n'
                                 'GNU General Public License v3.0\n')

    sys_exit(app.exec_())  # Run main loop


if __name__ == '__main__':
    main()
