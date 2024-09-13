from datetime import datetime as dt
import locale
from collections import defaultdict

from .requester import getAllJsonNewsData
from ..config.parsing_config import months_map


def get_russian_txt_date(dt_object):
    """Brings months in the correct case, i.e. "Январь - января" """
    locale.setlocale(locale.LC_TIME, "ru")
    russian_date = dt_object.strftime("%d %B %Y").lower()
    for nominal_case, genetive_case in months_map.items():
        if nominal_case in russian_date:
            proper_case = russian_date.replace(nominal_case, genetive_case)
            return proper_case


def parseNewsData():
    """
    Parses news data in json and returns title, timestamp and date-title (ru) of a news-card
    """
    locale.setlocale(locale.LC_TIME, "ru")
    list_of_dicts = getAllJsonNewsData()
    cards_by_month_list = defaultdict(list)
    for dict in list_of_dicts:
        for card in dict["index"]:
            dt_object = dt.fromtimestamp(card.get("date"))
            key = f"{dt_object.month}.{dt_object.year}"
            russian_date = get_russian_txt_date(dt_object)
            title = card.get("description")
            cards_by_month_list[str(key)].append(
                {
                    "Timestamp": dt_object.timestamp(),
                    "Date_title": russian_date,
                    "Title": title,
                }
            )
    return cards_by_month_list
