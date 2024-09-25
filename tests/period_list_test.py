from datetime import date
import pytest
from src.services.period_list import get_period_list, get_start_index, get_finish_index
from tests.test_data.period_list_data import *


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            5,
            date(year=2024, month=8, day=10),
            date(year=2024, month=8, day=15),
        ),
    ],
)
def test_start_date_index_with_more_than_one_news_for_the_day(
    input, expected, start_date, end_date
):
    """If there is more than one news for the day,
    func should return first occurance of the selected date"""
    index = get_start_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            8,
            date(year=2024, month=8, day=10),
            date(year=2024, month=8, day=13),
        ),
    ],
)
def test_start_date_index_with_no_news_for_the_day(
    input, expected, start_date, end_date
):
    """If there is no news for the day, func should return
    index of the next news, which date is earlier"""
    index = get_start_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            0,
            date(year=2024, month=8, day=10),
            date(year=2024, month=8, day=18),
        ),
    ],
)
def test_start_date_index_with_later_date(input, expected, start_date, end_date):
    """If selected date is earlier than there are in the list,
    than func should return the first item in the list.
    e.g. first in the list: 17.08.2024, selected: 18.08.2024.
    Func should return index of the first item, which is for 17.09.2024"""
    index = get_start_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            7,
            date(year=2024, month=8, day=14),
            date(year=2024, month=8, day=16),
        ),
    ],
)
def test_finish_date_index_for_one_news_in_day(input, expected, start_date, end_date):
    index = get_finish_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            6,
            date(year=2024, month=8, day=15),
            date(year=2024, month=8, day=17),
        ),
    ],
)
def test_finish_date_index_for_multiple_news_in_day(
    input, expected, start_date, end_date
):
    index = get_finish_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            29,
            date(year=2024, month=8, day=3),
            date(year=2024, month=8, day=17),
        ),
    ],
)
def test_finish_date_index_with_earlier_date(input, expected, start_date, end_date):
    index = get_finish_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            7,
            date(year=2024, month=8, day=13),
            date(year=2024, month=8, day=16),
        ),
    ],
)
def test_finish_date_index_with_no_news_for_the_day(
    input, expected, start_date, end_date
):
    """If there is no news for the day, func should return
    index of the next news, which date is earlier"""
    index = get_finish_index(input, start_date=start_date, end_date=end_date)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected, start_date, end_date",
    [
        (
            raw_period_list_test_input,
            raw_period_list_test_output,
            date(year=2024, month=8, day=11),
            date(year=2024, month=8, day=15),
        ),
    ],
)
def test_raw_list_slicing_output(input, expected, start_date, end_date):
    result = get_period_list(input, start_date=start_date, end_date=end_date)
    assert result == expected
    assert len(result) == len(raw_period_list_test_output)
