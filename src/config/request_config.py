
PAGE_SIZE = 24
"""
Max quantity in one page or one request
"""
REQUEST_SIZE = 24
"""
Optimal and max size for a request
"""
FIRST_REQUEST = 0
"""
The latest news card is number 0
"""
post_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "Origin": "https://president.gov.by",
    "Referer": "https://president.gov.by/",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.}",
}
"""
Headers from dev tools 
"""
