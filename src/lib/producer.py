
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
from lib.checker import *
import time


def serializer(r: CheckerResults):
    return json.dumps(r._asdict()).encode("utf-8")


def send_checker_results_to_kafka(results: List[CheckerResults],
                                  sleep_interval: int = 1):
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        security_protocol="SSL",
        ssl_cafile=FILE_SSL_CAFILE,
        ssl_certfile=FILE_SSL_CERTFILE,
        ssl_keyfile=FILE_SSL_KEYFILE,
    )

    for i, item in enumerate(results):
        message = serializer(item)
        print("Sending: {}".format(message))
        producer.send(KAFKA_TOPIC, message)
        time.sleep(sleep_interval)
    # Force sending of all messages
    producer.flush()

