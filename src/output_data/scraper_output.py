from datetime import datetime as dt
import locale
import os

from .scraper_docx import create_doc
from ..config.exceptions import SavePathDoesNotExistException


def check_save_loc(save_location: str, add_folder: bool):
    dt_now = (dt.now()).strftime("%d.%m.%Y")
    final_save_path = save_location
    if add_folder == True:
        final_save_path = f"{save_location}/Results {dt_now}"
        if not os.path.exists(final_save_path):
            os.makedirs(final_save_path)
    if not os.path.exists(final_save_path):
        raise SavePathDoesNotExistException
    return final_save_path


def create_filename(savelocation, date_string):
    return f"{savelocation}/{date_string} Полит. информирование.docx"


def get_date_string_mon_num(timestamp):
    locale.setlocale(locale.LC_TIME, "ru")
    dt_obj = dt.fromtimestamp(timestamp)
    return dt_obj.strftime("%m.%Y").lower()


def get_date_string_mon_name(timestamp):
    locale.setlocale(locale.LC_TIME, "ru")
    dt_obj = dt.fromtimestamp(timestamp)
    return dt_obj.strftime("%B %Y").lower()


def output_results(news_dict: dict, save_location: str, add_save_folder: bool):
    """Outputs results into folder results"""

    save_location = check_save_loc(save_location, add_save_folder)

    for key in news_dict:
        timestamp = news_dict[key][0]["Timestamp"]
        date_string = get_date_string_mon_name(timestamp)
        filename_date = get_date_string_mon_num(timestamp)
        filename = create_filename(save_location, filename_date)
        create_doc(news_dict[key], filename, date_string)
