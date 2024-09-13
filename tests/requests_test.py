from src.get_data.requester import jsonRequest
from src.get_data.requester import getAllJsonNewsData


def test_request_200():
    response = jsonRequest(1)
    assert response["total_results"] > 0


def test_all_json_properly_parsed():
    result = getAllJsonNewsData()
    total_results = result[0]["total_results"]
    tmp = 0
    for item in result:
        tmp += len(item["index"])
    assert total_results == tmp
