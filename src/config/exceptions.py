class NoInternetException(Exception):
    """Thrown when a query is made but host is not connected to Internet"""

    pass


class SavePathDoesNotExistException(Exception):
    """Thrown when chosen save path does not exist"""

    pass
