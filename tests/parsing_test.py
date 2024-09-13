import datetime as dt
import pytest
from src.get_data.parse_json import get_russian_txt_date


@pytest.mark.parametrize(
    "input, expected",
    [
        (dt.datetime(year=2024, month=9, day=1), "01 сентября 2024"),
        (dt.datetime(year=2025, month=1, day=23), "23 января 2025"),
    ],
)
def test_bring_date_to_case(input, expected):
    tmp = get_russian_txt_date(input)
    assert (tmp == expected)
