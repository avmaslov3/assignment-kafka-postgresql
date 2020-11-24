"""
Kafka producer (check website) -> Kafka topic -> Kafka consumer -> PostgreSQL
"""
import requests
from lib.common import *


def checker(url: str = "https://www.python.org/",
            retrieve_page_text: bool = False) -> CheckerResults:
    """
    The website checker should perform the checks periodically and collect the
    - HTTP response time,
    - error code returned,
    - as well as optionally checking the returned page contents for a regexp
    pattern that is expected to be found on the page.
    """
    r = requests.head(url)
    response_time_seconds = r.elapsed.total_seconds()
    status_code = r.status_code
    web_page_text = None
    if retrieve_page_text:
        web_page_text = requests.get(url).text[:50]
    result = CheckerResults(status_code, response_time_seconds, web_page_text)
    return result


if __name__ == '__main__':
    print(checker())
