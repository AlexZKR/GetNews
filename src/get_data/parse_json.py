from datetime import datetime as dt
import locale
from collections import defaultdict

from .requester import getAllJsonNewsData


def create_dt_object(date) -> dt:
    dt_object = dt.fromtimestamp(date)
    return dt_object


def parseNewsData():
    """
    Parses news data in json and returns title, timestamp and date-title (ru) of a news-card
    """
    locale.setlocale(locale.LC_TIME, "ru")
    list_of_dicts = getAllJsonNewsData()
    cards_by_month_list = defaultdict(list)
    for dict in list_of_dicts:
        for card in dict["index"]:
            dt_object = create_dt_object(card.get("date"))
            year_month = (dt_object.year, dt_object.month)
            russian_date = dt_object.strftime("%d %B %Y")
            title = card.get("description")
            cards_by_month_list[str(year_month)].append(
                {
                    "Timestamp": dt_object.timestamp(),
                    "Date_title": russian_date,
                    "Title": title,
                }
            )
    return cards_by_month_list
