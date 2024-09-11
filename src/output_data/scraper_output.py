from datetime import datetime as dt
import os

from .scraper_docx import import_to_doc
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


def out_put_doc(config_dict, month_news_list):
    doc = (import_to_doc(month_news_list, config_dict),)


def output_results(news_info: list, save_location: str, add_save_folder: bool):
    """Outputs results into folder results"""

    save_location = check_save_loc(save_location, add_save_folder)

    for mont_news_items in news_info:

        config_dict = create_config_dict(
            save_location, month_news_list[0]["Timestamp"], date_title_str
        )
        out_put_doc(config_dict, month_news_list)
