import os

from .scraper_docx import create_doc
from ..config.exceptions import SavePathDoesNotExistException
from src.get_data.data_conversion import *


def check_save_loc(save_location: str, add_folder: bool):
    if not os.path.exists(save_location):
        raise SavePathDoesNotExistException
    dt_now = get_now_full_str()
    final_save_path = save_location
    if add_folder == True:
        final_save_path = f"{save_location}/Results {dt_now}"
        try:
            os.makedirs(final_save_path)
        except Exception as e:
            if isinstance(e, FileExistsError):
                pass
            else:
                raise e
    return final_save_path


def create_filename(savelocation, date_string):
    return f"{savelocation}/{date_string} Полит. информирование.docx"


def get_date_string_mon_name(date_string):
    locale.setlocale(locale.LC_TIME, "ru")
    dt_obj = dt.strptime(date_string, "%m.%Y")
    return dt_obj.strftime("%B %Y").lower()


def output_by_months(news: tuple, save_location: str, add_save_folder: bool):
    """Outputs results into folder results"""
    save_location = check_save_loc(save_location, add_save_folder)
    for key in news:
        timestamp = news[key][0]["Timestamp"]
        header_date = get_mon_ru_str(key)
        filename_date = get_mon_date_str(timestamp)
        filename = create_filename(save_location, filename_date)
        create_doc(news[key], filename, header_date)


def output_by_period(news: tuple, save_location: str, add_save_folder: bool):
    """Outputs results into folder results"""
    period_string = news[0]
    save_location = check_save_loc(save_location, add_save_folder)
    filename = create_filename(save_location, period_string)
    create_doc(news[1], filename, period_string)
