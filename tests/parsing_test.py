import datetime as dt
import pytest

from src.get_data.parse_json import parseRawData
from src.get_data.parse_json import get_cased_rus_txt_date
from src.get_data.parse_json import sort_by_month
from tests.test_data.raw_parsing_data import *


@pytest.mark.parametrize(
    "input, expected",
    [
        (dt.datetime(year=2024, month=9, day=1), "01 сентября 2024"),
        (dt.datetime(year=2025, month=1, day=23), "23 января 2025"),
    ],
)
def test_bring_date_to_case(input, expected):
    tmp = get_cased_rus_txt_date(input)
    assert tmp == expected


@pytest.mark.parametrize(
    "input, expected",
    [(raw_news_test_input, raw_news_test_output)],
)
def test_parse_raw_dicts(input, expected):
    parsed = parseRawData(input)
    for i in range(len(input)):
        assert parsed[i] == expected[i]


@pytest.mark.parametrize(
    "input, expected",
    [(raw_sort_by_month_test_input, raw_sort_by_month_test_output)],
)
def test_sort_by_months(input, expected):
    res = sort_by_month(input)
    assert res == expected
