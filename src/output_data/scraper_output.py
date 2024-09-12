from datetime import datetime as dt
import locale
import os

from .scraper_docx import create_doc
from ..config.exceptions import SavePathDoesNotExistException


def create_config_dict(save_location, timestamp, date_title_str):
    return {
        "save_location": save_location,
        "now_date_title": (dt.now()).strftime("%d.%m.%Y"),
        "timestamp": timestamp,
        "news_date_title": date_title_str,
    }


def check_save_loc(save_location: str, add_folder: bool):
    dt_now = (dt.now()).strftime("%d.%m.%Y")
    final_save_path = save_location
    if add_folder == True:
        final_save_path = f"{save_location}/Results {dt_now}"
        if not os.path.exists(final_save_path):
            os.makedirs(final_save_path)
    if not os.path.exists(final_save_path):
        raise SavePathDoesNotExistException


def create_filename(savelocation, date_string):
    return f"{savelocation}/Полит. информирование {date_string}.docx"


def get_date_string(timestamp):
    locale.setlocale(locale.LC_TIME, "ru")
    dt_obj = dt.fromtimestamp(timestamp)
    return dt_obj.strftime("%B %Y").lower()


def output_results(news_info: list, save_location: str, add_save_folder: bool):
    """Outputs results into folder results"""

    save_location = check_save_loc(save_location, add_save_folder)

    for month_news_items in news_info:
        date_string = get_date_string(month_news_items["Timestamp"])
        filename = create_filename(save_location, date_string)
        create_doc(month_news_items, filename, date_string)
