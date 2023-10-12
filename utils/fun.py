import json
import os
from datetime import *


def read_json():
    """
    Функция открытия файла джисон
    """
    info_json = os.path.join('..', 'utils', 'operations.json')
    with open(info_json, encoding='utf-8') as file:
        return json.load(file)


def delete_void_list_(check):
    """
    Удаление пустого списка в файле
    """
    check_full = []
    for c in check:
        if c == {}:
            continue
        else:
            check_full.append(c)
    return check_full


def check_sorting(check_full):
    """
    Функция сортировки
    """
    check_sort = sorted(check_full, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    return check_sort


def get_executed(check_sort):
    """
    Функция поиска подходящего платежа
    """
    info_executed = []
    for items in check_sort:
        if "state" in items and items["state"] == "EXECUTED":
            info_executed.append(items)
    return info_executed
