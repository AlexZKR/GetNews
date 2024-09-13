import datetime as dt
import pytest

from src.get_data.parse_json import parseRawData
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
    assert tmp == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                {
                    "index": [
                        {
                            "id": 69289,
                            "title": "Соболезнование Президенту Социалистической Республики Вьетнам То Ламу",
                            "description": "Президент Беларуси Александр Лукашенко направил соболезнование Генеральному секретарю Центрального комитета Коммунистической партии Вьетнама, Президенту Социалистической Республики Вьетнам То Ламу в связи с жертвами тайфуна Яги.",
                            "tags": [{...}],
                            "category": [{...}],
                            "url": "/ru/events/soboleznovanie-prezidentu-socialisticeskoj-respubliki-v-etnam-to-lamu",
                            "dateTitle": "13 сентября 2024",
                            "sortValueBasedOnDate": 0.99,
                            "date": 1726239794,
                            "className": "event",
                            "image": "",
                            "mainImage": "",
                            "mainImageHtml": "",
                            "photoSize": "0",
                            "audioSize": "0",
                            "videoSize": "0",
                            "score": 8.716461,
                            "sort": [1726239794, "69289"],
                            "highlight": [],
                        }
                    ]
                }
            ],
            {
                "Timestamp": 1726239794,
                "Date_title": "13 сентября 2024",
                "Title": "Президент Беларуси Александр Лукашенко направил соболезнование Генеральному секретарю Центрального комитета Коммунистической партии Вьетнама, Президенту Социалистической Республики Вьетнам То Ламу в связи с жертвами тайфуна Яги.",
            },
        )
    ],
)
def test_parse_raw_dicts(input, expected):
    parsed = parseRawData(input)
    assert parsed[0] == expected
