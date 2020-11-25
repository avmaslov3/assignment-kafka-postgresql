
"""
- Kafka producer which periodically checks the target websites and sends the
check results to a Kafka topic
- Kafka consumer storing the data to an Aiven PostgreSQL database.

https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

"""
from kafka import KafkaProducer
from typing import List
from lib.settings import *
from lib.common import *
import json
import time
import requests
from loguru import logger
import argparse
import sys

parser = argparse.ArgumentParser('REPL')
parser.add_argument("url")
parser.add_argument('--key-file', help='Key file path')
args = parser.parse_args()

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG",
           rotation="1 MB", compression="zip")


@logger.catch
def checker(url: str = "https://www.python.org/",
            retrieve_page_text: bool = False) -> CheckerResults:
    """
    TODO: The website checker should perform the checks periodically and
    collect the
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
    web_page_text = None
    if retrieve_page_text:
        web_page_text = requests.get(url).text[:50]
    result = CheckerResults(status_code, response_time_seconds, web_page_text)
    return result


@logger.catch
def send_checker_results_to_kafka(results: List[CheckerResults],
                                  sleep_interval: int = 1) -> None:
    """
    Based on
    https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
    """
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        security_protocol="SSL",
        ssl_cafile=FILE_SSL_CAFILE,
        ssl_certfile=FILE_SSL_CERTFILE,
        ssl_keyfile=FILE_SSL_KEYFILE,
    )

    for i, item in enumerate(results):
        message = serializer(item)
        logger.info("Sending: {}".format(message))
        producer.send(KAFKA_TOPIC, message)
    # Force sending of all messages
    producer.flush()


def serializer(r: CheckerResults):
    return json.dumps(r._asdict()).encode("utf-8")


if __name__ == "__main__":
    try:
        while True:
            if args.url:
                metrics = checker(args.url)
                logger.info(metrics)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Buy!")

