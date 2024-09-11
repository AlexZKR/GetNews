from datetime import datetime as dt
import os, json
from collections import defaultdict

from .scraper_docx import import_to_doc


def create_config_dict(save_location, timestamp, date_title_str):
    return {
        "save_location": save_location,
        "now_date_title": (dt.now()).strftime("%d.%m.%Y"),
        "timestamp": timestamp,
        "news_date_title": date_title_str,
    }


def check_save_loc(save_location: str):
    dt_now = (dt.now()).strftime("%d.%m.%Y")
    if not os.path.exists(f"{save_location}/Results {dt_now}"):
        os.makedirs(f"{save_location}/Results {dt_now}")


def out_put_doc(config_dict, month_news_list):
    doc = (import_to_doc(month_news_list, config_dict),)


def output_results(
    news_info: defaultdict,
    save_location: str,
):
    """Outputs results in txt and json by months into folder "Results" """

    check_save_loc(save_location=save_location)
    for date_title_str, month_news_list in news_info.items():
        # for date_title_str, month_news_list in dict_list.items():
        config_dict = create_config_dict(
            save_location, month_news_list[0]["Timestamp"], date_title_str
        )
        out_put_doc(config_dict, month_news_list)
