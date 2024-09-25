from src.services.data_conversion import get_date_obj_ts


def get_period_list(news_list: list, start_date, end_date) -> list:
    start = get_start_index(news_list, start_date, end_date)
    end = get_finish_index(news_list, start_date, end_date)
    return news_list[start:end]


def get_start_index(news_list: list, start_date, end_date):
    first_news_date = get_date_obj_ts(news_list[0]["Timestamp"])
    if first_news_date < end_date:
        return 0

    for index, news_card in enumerate(news_list):
        current_news_date = get_date_obj_ts(news_card["Timestamp"])

        if current_news_date <= end_date:
            return index
    return -1


def get_finish_index(news_list: list, start_date, end_date):
    last_news_date = get_date_obj_ts(news_list[len(news_list) - 1]["Timestamp"])
    if start_date < last_news_date:
        return len(news_list)

    for index, dict in enumerate(news_list):
        current_news_date = get_date_obj_ts(dict["Timestamp"])
        if current_news_date == start_date:
            next_dict = news_list[index + 1]
            next_news_date = get_date_obj_ts(next_dict["Timestamp"])
            if next_news_date < current_news_date:
                return news_list.index(dict)
    return -1
