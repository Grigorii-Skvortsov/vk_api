from pandas import DataFrame
from requests import get
from datetime import datetime
from time import sleep, mktime  # sleep(1) - заснуть на 1 секунду
from sys import argv as sys_argv, exit as sys_exit
from PyQt5 import QtWidgets
from ui_window_main import Ui_MainWindow
from ui_widget_friends_get import Ui_MainWindow_Friends_Get
from ui_widget_newsfeed_search import Ui_MainWindow_Newsfeed_Search
from ui_widget_photos_search import Ui_MainWindow_Photos_Search
from ui_widget_groups_getMembers import Ui_MainWindow_Groups_GetMembers

global ACCESS_TOKEN, PHOTOS_SEARCH_V, NEWSFEED_SEARCH_V, FRIENDS_GET_V, GROUPS_GETMEMBERS_V, USERS_GET_V, GROUPS_GET_BY_ID_V
# open('C:/Google Drive/program/matirials_for_vk_api/token.txt').read() здесь вы указываете путь к своему токену доступа
ACCESS_TOKEN = open('C:/Google Drive/program/matirials_for_vk_api/token.txt').read()
PHOTOS_SEARCH_V = 5.126
NEWSFEED_SEARCH_V = 5.107
FRIENDS_GET_V = 5.107
GROUPS_GETMEMBERS_V = 5.107
USERS_GET_V = 5.107
GROUPS_GET_BY_ID_V = 5.107

if True:  # здесь свёрнуты функции делегирования
    # опишем фукции кнопок меню, делегирующие задачу в общую функцию с передачей номера окна и типа поиска
    def connect_push_button_find_1():
        searched_object = main_menu.comboBox_what_find_1.currentText()
        if searched_object == 'Newsfeed':
            push_button_find(0, searched_object)
        elif searched_object == 'Photos':
            push_button_find(0, searched_object)
        elif searched_object == 'Friends':
            push_button_find(0, searched_object)
        elif searched_object == 'Groups Members':
            push_button_find(0, searched_object)
        else:
            main_menu.textBrowser.append('Выберете, что вы хотите искать')


    def connect_push_button_find_2():
        searched_object = main_menu.comboBox_what_find_2.currentText()
        if searched_object == 'Newsfeed':
            push_button_find(1, searched_object)
        elif searched_object == 'Photos':
            push_button_find(1, searched_object)
        elif searched_object == 'Friends':
            push_button_find(1, searched_object)
        elif searched_object == 'Groups Members':
            push_button_find(1, searched_object)
        else:
            main_menu.textBrowser.append('Выберете, что вы хотите искать')


    # функционал кнопки "clear"
    def connect_push_button_newsfeed_search_clear_1():
        push_button_something_search_clear(0, 'newsfeed.search')


    def connect_push_button_photos_search_clear_1():
        push_button_something_search_clear(0, 'photos.search')


    def connect_push_button_friends_get_clear_1():
        push_button_something_search_clear(0, 'friends.get')


    def connect_push_button_groups_getMembers_clear_1():
        push_button_something_search_clear(0, 'groups.getMembers')


    def connect_push_button_newsfeed_search_clear_2():
        push_button_something_search_clear(1, 'newsfeed.search')


    def connect_push_button_photos_search_clear_2():
        push_button_something_search_clear(1, 'photos.search')


    def connect_push_button_friends_get_clear_2():
        push_button_something_search_clear(1, 'friends.get')


    def connect_push_button_groups_getMembers_clear_2():
        push_button_something_search_clear(1, 'groups.getMembers')


    # функционал кнопки "load"
    def connect_push_button_newsfeed_search_load_1():
        push_button_something_search_load(0, 'newsfeed.search')


    def connect_push_button_photos_search_load_1():
        push_button_something_search_load(0, 'photos.search')


    def connect_push_button_friends_get_load_1():
        push_button_something_search_load(0, 'friends.get')


    def connect_push_button_groups_getMembers_load_1():
        push_button_something_search_load(0, 'groups.getMembers')


    def connect_push_button_newsfeed_search_load_2():
        push_button_something_search_load(1, 'newsfeed.search')


    def connect_push_button_photos_search_load_2():
        push_button_something_search_load(1, 'photos.search')


    def connect_push_button_friends_get_load_2():
        push_button_something_search_load(1, 'friends.get')


    def connect_push_button_groups_getMembers_load_2():
        push_button_something_search_load(1, 'groups.getMembers')


    # функционал кнопки "save"
    def connect_push_button_newsfeed_search_save_1():
        push_button_something_search_save(0, 'newsfeed.search')


    def connect_push_button_photos_search_save_1():
        push_button_something_search_save(0, 'photos.search')


    def connect_push_button_friends_get_save_1():
        push_button_something_search_save(0, 'friends.get')


    def connect_push_button_groups_getMembers_save_1():
        push_button_something_search_save(0, 'groups.getMembers')


    def connect_push_button_newsfeed_search_save_2():
        push_button_something_search_save(1, 'newsfeed.search')


    def connect_push_button_photos_search_save_2():
        push_button_something_search_save(1, 'photos.search')


    def connect_push_button_friends_get_save_2():
        push_button_something_search_save(1, 'friends.get')


    def connect_push_button_groups_getMembers_save_2():
        push_button_something_search_save(1, 'groups.getMembers')


def push_button_find(i: int, searched_object: str):
    """i - widget number,
    searched_object - what we will looking for"""
    line_inspector()
    if searched_object == 'Newsfeed':
        WidgetNewsfeedSearch[i].show()
    elif searched_object == 'Photos':
        WidgetPhotosSearch[i].show()
    elif searched_object == 'Friends':
        WidgetFriendsGet[i].show()
    elif searched_object == 'Groups Members':
        WidgetGroupsGetMembers[i].show()


def push_button_something_search_load(i: int, request_type: str):
    """i - widget number
    request_type - type of search"""
    line_inspector()
    request_status = False
    data[i][request_type] = []
    max_one_count = {  # максимальное количество в запросе за раз
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

    params = {'access_token': ACCESS_TOKEN}  # создадим словарь, который будет содержать параметры запросы
    # не надо делать так. Делай формиование списка параметров под одним условием
    if request_type == 'newsfeed.search':
        q = newsfeed_search[i].lineEdit_newsfeed_search_q.text()
        if q != '':  # в запросе обязательно должен быть текст
            q = str(q)
            params.update({'q': q})
            params.update({'v': NEWSFEED_SEARCH_V})
            params.update({'extended': 0})  # 1, если необходимо получить информацию о пользователе или сообществе

            latitude = newsfeed_search[i].lineEdit_newsfeed_search_latitude.text()
            longitude = newsfeed_search[i].lineEdit_newsfeed_search_longitude.text()
            if latitude != '' and longitude != '':
                latitude = float(latitude)
                longitude = float(longitude)
                params.update({'latitude': latitude})  # северная широта
                params.update({'longitude': longitude})  # восточная долгота

            start_time_day = newsfeed_search[i].lineEdit_newsfeed_search_start_time_day.text()
            start_time_month = newsfeed_search[i].lineEdit_newsfeed_search_start_time_month.text()
            start_time_year = newsfeed_search[i].lineEdit_newsfeed_search_start_time_year.text()
            if start_time_day != '' and start_time_month != '' and start_time_year != '':
                start_time_day = int(start_time_day)
                start_time_month = int(start_time_month)
                start_time_year = int(start_time_year)
                start_time = y_m_d_to_unix(start_time_year, start_time_month, start_time_day)
                params.update({'start_time': start_time})

            end_time_day = newsfeed_search[i].lineEdit_newsfeed_search_end_time_day.text()
            end_time_month = newsfeed_search[i].lineEdit_newsfeed_search_end_time_month.text()
            end_time_year = newsfeed_search[i].lineEdit_newsfeed_search_end_time_year.text()
            if end_time_day != '' and end_time_month != '' and end_time_year != '':
                end_time_day = int(end_time_day)
                end_time_month = int(end_time_month)
                end_time_year = int(end_time_year)
                end_time = y_m_d_to_unix(end_time_year, end_time_month, end_time_day)
                params.update({'end_time': end_time})
            request_status = True
            newsfeed_search[i].lineEdit_newsfeed_search_status.setText('Данные выгружены')
        else:
            newsfeed_search[i].lineEdit_newsfeed_search_status.setText('Ошибка запроса')
            main_menu.textBrowser.append('Для поиска по постам необходимо указать текст запроса')

    elif request_type == 'photos.search':
        q = photos_search[i].lineEdit_photos_search_q.text()
        latitude = photos_search[i].lineEdit_photos_search_lat.text()
        longitude = photos_search[i].lineEdit_photos_search_long.text()
        if q != '' or (latitude != '' and longitude != ''):  # в запросе обязательно должен быть текст или координаты
            q = str(q)
            params.update({'q': q})
            params.update({'offset': 0})  # изначальное смещение относительно первого результата
            params.update({'v': PHOTOS_SEARCH_V})

            latitude = photos_search[i].lineEdit_photos_search_lat.text()
            longitude = photos_search[i].lineEdit_photos_search_long.text()
            if latitude != '' and longitude != '':
                latitude = float(latitude)
                longitude = float(longitude)
                params.update({'lat': latitude})  # северная широта
                params.update({'long': longitude})  # восточная долгота

            radius = photos_search[i].lineEdit_photos_search_radius.text()
            if radius != '':
                radius = int(radius)
                params.update({'radius': radius})

            start_time_day = photos_search[i].lineEdit_photos_search_start_time_day.text()
            start_time_month = photos_search[i].lineEdit_photos_search_start_time_month.text()
            start_time_year = photos_search[i].lineEdit_photos_search_start_time_year.text()
            if start_time_day != '' and start_time_month != '' and start_time_year != '':
                start_time_day = int(start_time_day)
                start_time_month = int(start_time_month)
                start_time_year = int(start_time_year)
                start_time = y_m_d_to_unix(start_time_year, start_time_month, start_time_day)
                params.update({'start_time': start_time})

            end_time_day = photos_search[i].lineEdit_photos_search_end_time_day.text()
            end_time_month = photos_search[i].lineEdit_photos_search_end_time_month.text()
            end_time_year = photos_search[i].lineEdit_photos_search_end_time_year.text()
            if end_time_day != '' and end_time_month != '' and end_time_year != '':
                end_time_day = int(end_time_day)
                end_time_month = int(end_time_month)
                end_time_year = int(end_time_year)
                end_time = y_m_d_to_unix(end_time_year, end_time_month, end_time_day)
                params.update({'end_time': end_time})

            sort = int(photos_search[i].radioButton_photos_search_sort.isChecked())  # 1 - по лайкам, 0 - по дате
            params.update({'radius': sort})

            request_status = True
            photos_search[i].lineEdit_photos_search_status.setText('Данные выгружены')
        else:
            photos_search[i].lineEdit_photos_search_status.setText('Ошибка запроса')
            main_menu.textBrowser.append('Для поиска по фото необходимо указать текст запроса или координаты')

    elif request_type == 'friends.get':
        user_id = friends_get[i].lineEdit_friends_get_id.text()
        if user_id != '':
            user_id = int(user_id)
            params.update({'user_id': user_id})
            params.update({'v': FRIENDS_GET_V})
            params.update({'fields': 'city, country'})
            request_status = True
            friends_get[i].lineEdit_friends_get_status.setText('Данные выгружены')
        else:
            main_menu.textBrowser.append('Для поиска по друзьям необходимо указать ID пользователя')
            friends_get[i].lineEdit_friends_get_status.setText('Ошибка запроса')

    elif request_type == 'groups.getMembers':
        group_id = groups_getMembers[i].lineEdit_groups_getMembers_id.text()
        if group_id != '':
            group_id = int(group_id)
            params.update({'group_id': group_id})
            params.update({'v': GROUPS_GETMEMBERS_V})
            params.update({'fields': 'city, country'})
            request_status = True
            groups_getMembers[i].lineEdit_groups_getMembers_status.setText('Данные выгружены')
        else:
            groups_getMembers[i].lineEdit_groups_getMembers_status.setText('Ошибка запроса')
            main_menu.textBrowser.append('Для поиска по группам необходимо указать ID группы')

    # сформируем сам запрос
    if request_status:
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
            # откроем черный список для фильтрации
            black_list = open('black_list.csv', 'r').read()
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
                    data[i][request_type].append(
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
                         'post_source': ' '.join([item["post_source"][source] for source in item["post_source"]]),
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
                    data[i][request_type].append(
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
                    data[i][request_type].append(
                        {'id': this_id,
                         'link': '=HYPERLINK("{}", "{}")'.format(
                             f"https://vk.com/id{str(item['id']).replace('-', '')}", 'page link'),
                         'first_name': item['first_name'],
                         'last_name': item['last_name'],
                         'country': this_country,
                         'city': this_city,
                         })
        main_menu.textBrowser.append(f"{len(data[i][request_type])} результатов поиска загружено. Сохранить?")


def push_button_something_search_clear(i: int, request_type: str):
    """i - widget number
    request_type - type of search"""
    line_inspector()
    if request_type == 'newsfeed.search':
        newsfeed_search[i].lineEdit_newsfeed_search_status.setText('Данных нет')
        clearing_lines = [
            newsfeed_search[i].lineEdit_newsfeed_search_q,

            newsfeed_search[i].lineEdit_newsfeed_search_latitude,
            newsfeed_search[i].lineEdit_newsfeed_search_longitude,

            newsfeed_search[i].lineEdit_newsfeed_search_start_time_day,
            newsfeed_search[i].lineEdit_newsfeed_search_start_time_month,
            newsfeed_search[i].lineEdit_newsfeed_search_start_time_year,

            newsfeed_search[i].lineEdit_newsfeed_search_end_time_day,
            newsfeed_search[i].lineEdit_newsfeed_search_end_time_month,
            newsfeed_search[i].lineEdit_newsfeed_search_end_time_year,
        ]
    elif request_type == 'photos.search':
        photos_search[i].lineEdit_photos_search_status.setText('Данных нет')
        clearing_lines = [
            photos_search[i].lineEdit_photos_search_q,

            photos_search[i].lineEdit_photos_search_lat,
            photos_search[i].lineEdit_photos_search_long,
            photos_search[i].lineEdit_photos_search_radius,

            photos_search[i].lineEdit_photos_search_start_time_day,
            photos_search[i].lineEdit_photos_search_start_time_month,
            photos_search[i].lineEdit_photos_search_start_time_year,

            photos_search[i].lineEdit_photos_search_end_time_day,
            photos_search[i].lineEdit_photos_search_end_time_month,
            photos_search[i].lineEdit_photos_search_end_time_year,
        ]
    elif request_type == 'friends.get':
        friends_get[i].lineEdit_friends_get_status.setText('Данных нет')
        clearing_lines = [
            friends_get[i].lineEdit_friends_get_id,
        ]
    elif request_type == 'groups.getMembers':
        groups_getMembers[i].lineEdit_groups_getMembers_status.setText('Данных нет')
        clearing_lines = [
            groups_getMembers[i].lineEdit_groups_getMembers_id,
        ]
    data[i][request_type] = []
    for line in clearing_lines:
        line.clear()


def push_button_something_search_save(i: int, request_type: str):
    """i - widget number
    request_type - type of search"""
    line_inspector()
    status_line = {
        'newsfeed.search': newsfeed_search[i].lineEdit_newsfeed_search_status,
        'photos.search': photos_search[i].lineEdit_photos_search_status,
        'friends.get': friends_get[i].lineEdit_friends_get_status,
        'groups.getMembers': groups_getMembers[i].lineEdit_groups_getMembers_status,
    }
    if len(data[i][request_type]) > 0:
        csv_name = {
            'newsfeed.search': newsfeed_search[i].lineEdit_newsfeed_search_file_name.text(),
            'photos.search': photos_search[i].lineEdit_photos_search_file_name.text(),
            'friends.get': friends_get[i].lineEdit_friends_get_file_name.text(),
            'groups.getMembers': groups_getMembers[i].lineEdit_groups_getMembers_file_name.text(),
        }

        this_name = f"{csv_name[request_type]}_{str(i)}{request_type.replace('.', '')}.xlsx"

        data_frame = DataFrame.from_dict(data[i][request_type])  # преобразовываем в data frame
        data_frame.to_excel(this_name, index=False)  # перезаписываем файл в excel

        status_line[request_type].setText('Записано в файл')
        main_menu.textBrowser.append(f"В файл '{this_name}' сохранено {len(data[i][request_type])} id")
    else:
        push_button_something_search_load(i, request_type)


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


def push_button_find_intersections_find():
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
    push_button_find_intersections_find()
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


def push_button_black_list_seize():
    line_inspector()
    disignored_object = main_menu.lineEdit_black_list_object.text()
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


def push_button_black_list_display():
    line_inspector()
    with open('black_list.csv', 'r') as file:
        what_len = set()
        for item in file:
            what_len.add(item)
    main_menu.textBrowser.append(f"'black_list.csv' содержит {len(what_len)} элементов:")
    with open('black_list.csv', 'r') as file:
        for item in file:
            main_menu.textBrowser.append(item.replace('\n', ''))


def line_inspector():
    """Функция инспектирует на правильность заполнения полей ввода"""
    only_integro_lines_list = [  # список полей, где могут быть только целые числа
        main_menu.lineEdit_black_list_object,
        main_menu.lineEdit_get_group_id_id,
        main_menu.lineEdit_get_user_id_id,

        newsfeed_search[0].lineEdit_newsfeed_search_start_time_day,
        newsfeed_search[0].lineEdit_newsfeed_search_start_time_month,
        newsfeed_search[0].lineEdit_newsfeed_search_start_time_year,
        newsfeed_search[0].lineEdit_newsfeed_search_end_time_day,
        newsfeed_search[0].lineEdit_newsfeed_search_end_time_month,
        newsfeed_search[0].lineEdit_newsfeed_search_end_time_year,
        newsfeed_search[1].lineEdit_newsfeed_search_start_time_day,
        newsfeed_search[1].lineEdit_newsfeed_search_start_time_month,
        newsfeed_search[1].lineEdit_newsfeed_search_start_time_year,
        newsfeed_search[1].lineEdit_newsfeed_search_end_time_day,
        newsfeed_search[1].lineEdit_newsfeed_search_end_time_month,
        newsfeed_search[1].lineEdit_newsfeed_search_end_time_year,

        photos_search[0].lineEdit_photos_search_radius,
        photos_search[0].lineEdit_photos_search_end_time_day,
        photos_search[0].lineEdit_photos_search_end_time_month,
        photos_search[0].lineEdit_photos_search_end_time_year,
        photos_search[0].lineEdit_photos_search_start_time_day,
        photos_search[0].lineEdit_photos_search_start_time_month,
        photos_search[0].lineEdit_photos_search_start_time_year,
        photos_search[1].lineEdit_photos_search_radius,
        photos_search[1].lineEdit_photos_search_end_time_day,
        photos_search[1].lineEdit_photos_search_end_time_month,
        photos_search[1].lineEdit_photos_search_end_time_year,
        photos_search[1].lineEdit_photos_search_start_time_day,
        photos_search[1].lineEdit_photos_search_start_time_month,
        photos_search[1].lineEdit_photos_search_start_time_year,
    ]

    maybe_float_lines_list = [  # список полей, где число может быть десятичным (например - координаты)
        newsfeed_search[0].lineEdit_newsfeed_search_latitude,
        newsfeed_search[0].lineEdit_newsfeed_search_longitude,
        newsfeed_search[1].lineEdit_newsfeed_search_latitude,
        newsfeed_search[1].lineEdit_newsfeed_search_longitude,

        photos_search[0].lineEdit_photos_search_lat,
        photos_search[0].lineEdit_photos_search_long,
        photos_search[1].lineEdit_photos_search_lat,
        photos_search[1].lineEdit_photos_search_long,
    ]

    text_lines_without_spaces = [  # список полей, где не должно быть пробелов
        main_menu.lineEdit_get_group_id_txt_id,
        main_menu.lineEdit_get_user_id_txt_id,

        main_menu.lineEdit_find_intersections_file_1,
        main_menu.lineEdit_find_intersections_file_2,
        main_menu.lineEdit_file_name,

        main_menu.lineEdit_integration_file_1,
        main_menu.lineEdit_integration_file_2,
        main_menu.lineEdit_integration_file_name,

        newsfeed_search[0].lineEdit_newsfeed_search_file_name,
        newsfeed_search[1].lineEdit_newsfeed_search_file_name,

        photos_search[0].lineEdit_photos_search_file_name,
        photos_search[1].lineEdit_photos_search_file_name,

        groups_getMembers[0].lineEdit_groups_getMembers_id,
        groups_getMembers[0].lineEdit_groups_getMembers_file_name,
        groups_getMembers[1].lineEdit_groups_getMembers_id,
        groups_getMembers[1].lineEdit_groups_getMembers_file_name,

        friends_get[0].lineEdit_friends_get_id,
        friends_get[0].lineEdit_friends_get_file_name,
        friends_get[1].lineEdit_friends_get_id,
        friends_get[1].lineEdit_friends_get_file_name,
    ]

    text_lines_list = [  # список полей, где может быть только текст (удалятся пробелы)
        newsfeed_search[0].lineEdit_newsfeed_search_q,
        newsfeed_search[1].lineEdit_newsfeed_search_q,

        photos_search[0].lineEdit_photos_search_q,
        photos_search[1].lineEdit_photos_search_q,
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
    global data, main_menu, friends_get, newsfeed_search, photos_search, groups_getMembers, \
        WidgetFriendsGet, WidgetNewsfeedSearch, WidgetPhotosSearch, WidgetGroupsGetMembers, \
        intersection_set, integration_set

    data = [  # данные, полученные в запросе. i - номер виджета, ключ словаря - тип запроса.
        {'newsfeed.search': [], 'photos.search': [], 'friends.get': [], 'groups.getMembers': []},
        {'newsfeed.search': [], 'photos.search': [], 'friends.get': [], 'groups.getMembers': []}
    ]

    intersection_set = set()
    integration_set = set()

    app = QtWidgets.QApplication(sys_argv)  # Create application - инициализация приложения
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню

    friends_get = []
    newsfeed_search = []
    photos_search = []
    groups_getMembers = []

    WidgetFriendsGet = []
    WidgetNewsfeedSearch = []
    WidgetPhotosSearch = []
    WidgetGroupsGetMembers = []

    for i in range(0, 2):  # создаём виджеты от 0 до 1 (две штуки)
        friends_get.append(Ui_MainWindow_Friends_Get())
        newsfeed_search.append(Ui_MainWindow_Newsfeed_Search())
        photos_search.append(Ui_MainWindow_Photos_Search())
        groups_getMembers.append(Ui_MainWindow_Groups_GetMembers())

        WidgetFriendsGet.append(QtWidgets.QMainWindow())
        WidgetNewsfeedSearch.append(QtWidgets.QMainWindow())
        WidgetPhotosSearch.append(QtWidgets.QMainWindow())
        WidgetGroupsGetMembers.append(QtWidgets.QMainWindow())

        friends_get[i].setupUi(WidgetFriendsGet[i])
        newsfeed_search[i].setupUi(WidgetNewsfeedSearch[i])
        photos_search[i].setupUi(WidgetPhotosSearch[i])
        groups_getMembers[i].setupUi(WidgetGroupsGetMembers[i])

    main_menu = Ui_MainWindow()
    main_menu.setupUi(MainWindow)
    MainWindow.show()

    main_menu.pushButton_get_group_id.clicked.connect(push_button_get_group_id)
    main_menu.pushButton_get_user_id.clicked.connect(push_button_get_user_id)
    main_menu.pushButton_find_1.clicked.connect(connect_push_button_find_1)
    main_menu.pushButton_find_2.clicked.connect(connect_push_button_find_2)

    main_menu.pushButton_find_intersections_find.clicked.connect(push_button_find_intersections_find)
    main_menu.pushButton_find_intersections_clear.clicked.connect(push_button_find_intersections_clear)
    main_menu.pushButton_find_intersections_save.clicked.connect(push_button_find_intersections_save)

    main_menu.pushButton_integration_find.clicked.connect(push_button_integration_find)
    main_menu.pushButton_integration_clear.clicked.connect(push_button_integration_clear)
    main_menu.pushButton_integration_save.clicked.connect(push_button_integration_save)

    main_menu.pushButton_black_list_add.clicked.connect(push_button_black_list_add)
    main_menu.pushButton_black_list_seize.clicked.connect(push_button_black_list_seize)
    main_menu.pushButton_black_list_display.clicked.connect(push_button_black_list_display)

    newsfeed_search[0].pushButton_newsfeed_search_load.clicked.connect(connect_push_button_newsfeed_search_load_1)
    newsfeed_search[0].pushButton_newsfeed_search_clear.clicked.connect(connect_push_button_newsfeed_search_clear_1)
    newsfeed_search[0].pushButton_newsfeed_search_save.clicked.connect(connect_push_button_newsfeed_search_save_1)
    newsfeed_search[1].pushButton_newsfeed_search_load.clicked.connect(connect_push_button_newsfeed_search_load_2)
    newsfeed_search[1].pushButton_newsfeed_search_clear.clicked.connect(connect_push_button_newsfeed_search_clear_2)
    newsfeed_search[1].pushButton_newsfeed_search_save.clicked.connect(connect_push_button_newsfeed_search_save_2)

    photos_search[0].pushButton_photos_search_load.clicked.connect(connect_push_button_photos_search_load_1)
    photos_search[0].pushButton_photos_search_clear.clicked.connect(connect_push_button_photos_search_clear_1)
    photos_search[0].pushButton_photos_search_save.clicked.connect(connect_push_button_photos_search_save_1)
    photos_search[1].pushButton_photos_search_load.clicked.connect(connect_push_button_photos_search_load_2)
    photos_search[1].pushButton_photos_search_clear.clicked.connect(connect_push_button_photos_search_clear_2)
    photos_search[1].pushButton_photos_search_save.clicked.connect(connect_push_button_photos_search_save_2)

    friends_get[0].pushButton_friends_get_load.clicked.connect(connect_push_button_friends_get_load_1)
    friends_get[0].pushButton_friends_get_clear.clicked.connect(connect_push_button_friends_get_clear_1)
    friends_get[0].pushButton_friends_get_save.clicked.connect(connect_push_button_friends_get_save_1)
    friends_get[1].pushButton_friends_get_load.clicked.connect(connect_push_button_friends_get_load_2)
    friends_get[1].pushButton_friends_get_clear.clicked.connect(connect_push_button_friends_get_clear_2)
    friends_get[1].pushButton_friends_get_save.clicked.connect(connect_push_button_friends_get_save_2)

    groups_getMembers[0].pushButton_groups_getMembers_load.clicked.connect(connect_push_button_groups_getMembers_load_1)
    groups_getMembers[0].pushButton_groups_getMembers_clear.clicked.connect(
        connect_push_button_groups_getMembers_clear_1)
    groups_getMembers[0].pushButton_groups_getMembers_save.clicked.connect(connect_push_button_groups_getMembers_save_1)
    groups_getMembers[1].pushButton_groups_getMembers_load.clicked.connect(connect_push_button_groups_getMembers_load_2)
    groups_getMembers[1].pushButton_groups_getMembers_clear.clicked.connect(
        connect_push_button_groups_getMembers_clear_2)
    groups_getMembers[1].pushButton_groups_getMembers_save.clicked.connect(connect_push_button_groups_getMembers_save_2)

    main_menu.textBrowser.append('Программа "Palantir" иницирована и готова к использованию\n'
                                 'Версия - Alpha 0.3\n'
                                 'Связь с автором - Григорий Скворцов GregoryValeryS@gmail.com\n'
                                 'GNU General Public License v3.0\n')

    sys_exit(app.exec_())  # Run main loop


if __name__ == '__main__':
    main()
