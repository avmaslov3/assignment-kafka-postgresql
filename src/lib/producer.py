
"""
- Kafka producer which periodically checks the target websites and sends the
check results to a Kafka topic
- Kafka consumer storing the data to an Aiven PostgreSQL database.

https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka

"""
from kafka import KafkaProducer, errors
from typing import List
from lib.common import *
import json
import time
import requests
from loguru import logger
import sys
from lib.settings import *

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG",
           rotation="1 MB", compression="zip")


@logger.catch
def measure_metrics(url: str,
                    retrieve_page_text: bool = False) -> ResponseMetrics:
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
    result = ResponseMetrics(status_code, response_time_seconds,
                             web_page_text, url)
    return result


producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_SERVER"),
    security_protocol="SSL",
    ssl_cafile=FILE_SSL_CAFILE,
    ssl_certfile=FILE_SSL_CERTFILE,
    ssl_keyfile=FILE_SSL_KEYFILE,
)


@logger.catch
def send_data_to_kafka(result: ResponseMetrics) -> None:
    """
    Based on https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
    """

    message = serializer(result)
    try:
        producer.send("KAFKA_TOPIC", message)
        producer.flush()
    except errors.KafkaTimeoutError as e:
        logger.info(e)
    finally:
        # TODO: Maybe this is not correct order as in the sample code messages
        #  are sent in iteration process
        # Force sending of all messages
        producer.flush()


def serializer(r: ResponseMetrics):
    checker_results_as_json = json.dumps(r._asdict()).encode("utf-8")
    return checker_results_as_json


def checker(url: str, max_n: int = None):
    count = 0
    try:
        while True:
            count += 1
            if max_n and count > max_n:
                break
            metrics = measure_metrics(url)
            logger.info("Received results from URL: {}".format(metrics))
            send_data_to_kafka(metrics)
            logger.info("Sent to Kafka service: {}".format(metrics))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Buy!")


if __name__ == "__main__":
    checker("https://docs.python.org/3/")
