from src.get_data.data_conversion import *

from .requester import getAllJsonNewsData


def parseRawData(raw_dicts=None):
    """
    Parses news data in json and returns title, timestamp and date-title (ru) of a news-card
    """
    if raw_dicts is None:
        raw_dicts = getAllJsonNewsData()
    parsed_dicts = []
    for dict in raw_dicts:
        for card in dict["index"]:
            dt_object = get_datetime_obj(card.get("date"))
            russian_date = get_cased_rus_txt_date(dt_object)
            title = card.get("description")
            parsed_dicts.append(
                {
                    "Timestamp": dt_object.timestamp(),
                    "Date_title": russian_date,
                    "Title": title,
                }
            )
    return parsed_dicts


def sort_by_month(raw_data):
    result = {}
    for item in raw_data:
        mon_str = get_mon_date_str(item["Timestamp"])
        if mon_str not in result:
            result[mon_str] = []
        result[mon_str].append(item)
    return result
