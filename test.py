from pandas import DataFrame, read_excel

def write_json_in_file(data):
    """функция получет json-данные и записывает их в файл data.json"""
    with open('data.json', 'w') as file:  # создаём/открываем файл data
        # и сохраняем данные файла в переменную file
        json.dump(data, file, indent=2, ensure_ascii=False)


def unix_to_d_m_y_str(unix: int) -> str:
    """Функция получет на вход время в unix-формате, возвращает словарь с годом, месяцем и днём"""
    return f"{datetime.fromtimestamp(unix).strftime('%d')}.{datetime.fromtimestamp(unix).strftime('%m')}.{datetime.fromtimestamp(unix).strftime('%Y')[2:]} "


def unix_to_y_m_d(unix: int) -> dict:
    """Функция получет на вход время в unix-формате, возвращает словарь с годом, месяцем и днём"""
    return {'y': datetime.datetime.fromtimestamp(unix).strftime('%Y'),
            'm': datetime.datetime.fromtimestamp(unix).strftime('%m'),
            'd': datetime.datetime.fromtimestamp(unix).strftime('%d')}



