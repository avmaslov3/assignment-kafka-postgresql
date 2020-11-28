
"""
- Kafka producer which periodically checks the target websites and sends the
check results to a Kafka topic
- Kafka consumer storing the data to an Aiven PostgreSQL database.

https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

"""
from kafka import KafkaProducer, errors
from lib.common import *
import json
import time
import requests
from loguru import logger
import sys
from lib.settings import *

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG",
           rotation="1 MB", compression="zip")


@logger.catch()
def checker(url: str,
            max_n: int = None,
            sleep_interval: float = 1.0,
            regexp_pattern: str = r"") -> None:
    """
    Main producer function.
    Send requests periodically to URL, collects response metrics, and sends
    them to Kafka service.
    :param url: Web page URL to monitor metrics from.
    :param max_n: Optional maximum number of requests, if None then forever.
    :param sleep_interval: Optional delay between requests.
    :param regexp_pattern: Optional regexp pattern to be searched in web
    page content.
    """
    count = 0
    try:
        while True:
            count += 1
            if max_n and count > max_n:
                break
            metrics = measure_metrics(url, regexp_pattern=regexp_pattern)
            send_to_kafka(metrics)
            logger.info("Received results from URL: {}".format(metrics))
            logger.info("Sent to Kafka service: {}".format(metrics))
            time.sleep(sleep_interval)
    except KeyboardInterrupt:
        print("Stop producer!")


@logger.catch
def measure_metrics(url: str,
                    regexp_pattern=None) -> ResponseMetrics:
    """
    The website checker performs checks periodically and collects
    - HTTP response time,
    - error code returned,
    - as well as optionally checking the returned page contents for a regexp
    pattern that is expected to be found on the page.
    """
    try:
        r = requests.head(url)
    except requests.exceptions.MissingSchema as e:
        logger.error(e)
        sys.exit(1)
    response_time_seconds = r.elapsed.total_seconds()
    status_code = r.status_code
    re_pattern_is_found = None
    if regexp_pattern is not None:
        web_page_text = requests.get(url).text
        re_pattern_is_found = check_re_pattern_page_text(web_page_text,
                                                         regexp_pattern)
    result = ResponseMetrics(status_code,
                             response_time_seconds,
                             re_pattern_is_found,
                             url)
    return result


@logger.catch
def send_to_kafka(result: ResponseMetrics) -> None:
    """
    Based on https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
    """
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        security_protocol="SSL",
        ssl_cafile=FILE_SSL_CAFILE,
        ssl_certfile=FILE_SSL_CERTFILE,
        ssl_keyfile=FILE_SSL_KEYFILE,
    )
    message = serializer(result)
    producer.send(KAFKA_TOPIC, message)
    # Force sending of all messages
    # TODO: not sure if needed
    producer.flush()


def serializer(r: ResponseMetrics):
    checker_results_as_json = json.dumps(r._asdict()).encode("utf-8")
    return checker_results_as_json
