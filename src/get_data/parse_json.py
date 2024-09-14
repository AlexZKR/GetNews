from datetime import datetime as dt
import datetime
import locale
from collections import defaultdict

from .requester import getAllJsonNewsData
from ..config.parsing_config import months_map


def parseRawData(raw_dicts=None):
    """
    Parses news data in json and returns title, timestamp and date-title (ru) of a news-card
    """
    if raw_dicts is None:
        raw_dicts = getAllJsonNewsData()
    parsed_dicts = []
    for dict in raw_dicts:
        for card in dict["index"]:
            dt_object = dt.fromtimestamp(card.get("date"))
            russian_date = get_russian_txt_date(dt_object)
            title = card.get("description")
            parsed_dicts.append(
                {
                    "Timestamp": dt_object.timestamp(),
                    "Date_title": russian_date,
                    "Title": title,
                }
            )
    return parsed_dicts


def get_total_results(data):
    total_results = len(data)
    if total_results <= 0:
        return f"Получено {total_results} новостных карточек. Что-то пошло не так"
    else:
        return f"Получено {total_results} новостных карточек"


def sort_by_month(raw_data):
    result = {}
    for item in raw_data:
        mon_str = get_mon_digit_str(item["Timestamp"])
        if mon_str not in result:
            result[mon_str] = []
        result[mon_str].append(item)
    return result


def get_mon_digit_str(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%m.%Y")


def get_mon_ru_str(string):
    locale.setlocale(locale.LC_TIME, "ru")
    return datetime.datetime.strptime(string, "%m.%Y").strftime("%B %Y")


def get_russian_txt_date(dt_object):
    """Brings months in the correct case, i.e. "Январь - января" """
    locale.setlocale(locale.LC_TIME, "ru")
    russian_date = dt_object.strftime("%d %B %Y").lower()
    for nominal_case, genetive_case in months_map.items():
        if nominal_case in russian_date:
            proper_case = russian_date.replace(nominal_case, genetive_case)
            return proper_case

    # locale.setlocale(locale.LC_TIME, "ru")
    # list_of_dicts = getAllJsonNewsData()
    # cards_by_month_list = defaultdict(list)
    # for dict in list_of_dicts:
    #     for card in dict["index"]:
    #         dt_object = dt.fromtimestamp(card.get("date"))
    #         key = f"{dt_object.month}.{dt_object.year}"
    #         russian_date = get_russian_txt_date(dt_object)
    #         title = card.get("description")
    #         cards_by_month_list[str(key)].append(
    #             {
    #                 "Timestamp": dt_object.timestamp(),
    #                 "Date_title": russian_date,
    #                 "Title": title,
    #             }
    #         )
