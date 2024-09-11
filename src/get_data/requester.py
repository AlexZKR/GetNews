import requests

from src.config.request_config import *
from src.config.exceptions import NoInternetException


def getAllJsonNewsData() -> list:
    """
    Returns all news cards available in json format
    """
    final_results = []  # final big dict of dicts to which all requests are appended
    request_result = []  # result of one request
    request_starting_from = FIRST_REQUEST  # size of one request starting with 0

    while True:
        # just making requests with incremeting request_size in query string of request
        # then appending result of request to the final json file and returning it
        request_result = jsonRequest(req_from=request_starting_from)
        if isinstance(request_result, dict):
            if not request_result["index"]:
                # print(f"Contents are empty in request size {request_starting_from}")
                break  # checking if content of json is empty
            final_results.append(request_result)
            request_starting_from += REQUEST_SIZE
    return final_results


def jsonRequest(req_from: int):
    """
    Returns a data in a json file from one request

    Args:
        request_size (int): incremented in a cycle to reach the bottom of site
    """
    postURL = f"https://search.president.gov.by/ru/search/show-more-category/event/{req_from}/{PAGE_SIZE}"
    try:
        result = requests.post(postURL, headers=post_headers)
        return result.json()
    except requests.exceptions.JSONDecodeError:
        print("Json is either empty or bad formated")
    except Exception as e:
        if isinstance(e, requests.exceptions.ConnectionError):
            raise NoInternetException
        else:
            print(f"Exception thrown:\n {e}")
