import locale
from datetime import date
import datetime as dt

from ..config.parsing_config import months_map


def get_full_date_str(timestamp):
    return date.fromtimestamp(timestamp).strftime("%d.%m.%Y")


def get_now_full_str():
    return dt.datetime.now().strftime("%d.%m.%Y")


def get_mon_date_str(timestamp):
    return dt.datetime.fromtimestamp(timestamp).strftime("%m.%Y")


def get_date_obj(timestamp):
    return date.fromtimestamp(timestamp)


def get_datetime_obj(timestamp):
    return dt.datetime.fromtimestamp(timestamp)


def get_mon_ru_str(string):
    locale.setlocale(locale.LC_TIME, "ru")
    return dt.datetime.strptime(string, "%m.%Y").strftime("%B %Y")


def get_cased_rus_txt_date(dt_object: dt):
    """Brings months in the correct case, i.e. "Январь - января" """
    locale.setlocale(locale.LC_TIME, "ru")
    russian_date = dt_object.strftime("%d %B %Y").lower()
    for nominal_case, genetive_case in months_map.items():
        if nominal_case in russian_date:
            proper_case = russian_date.replace(nominal_case, genetive_case)
            return proper_case
