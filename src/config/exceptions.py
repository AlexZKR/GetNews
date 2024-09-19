class NoInternetException(Exception):
    """Thrown when a query is made but host is not connected to Internet"""

    pass


class SavePathDoesNotExistException(Exception):
    """Thrown when chosen save path does not exist"""

    pass


class NoMonthsChosenException(Exception):
    """Thrown when saving initialized but no months were chosen in the table"""

    pass


class NoPeriodChosenException(Exception):
    """Thrown when user did not query news for period in Period Tab"""

    pass
