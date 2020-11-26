"""
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
"""
from lib.settings import *
from lib.database import *
from kafka import KafkaConsumer
from loguru import logger
import time
import json
from typing import List
from lib.common import *


@logger.catch()
def consumer(sleep_interval: float = 1.0) -> None:
    """
    Main consumer function.
    Retrieves messages from Kafka topic and sends them to PostgreSQL.
    :param sleep_interval: Optional delay between request to Kafka service.
    """
    try:
        while True:
            data_kafka = read_from_kafka()
            if len(data_kafka) > 0:
                logger.info(f"Received data from Kafka. len(data) ="
                            f" {len(data_kafka)}")
                for metrics in data_kafka:
                    send_to_database(metrics)
                    logger.info(".. Sent to database")
            else:
                logger.info("Kafka topic is empty")
            time.sleep(sleep_interval)
    except KeyboardInterrupt:
        print("Stop consumer!")


@logger.catch()
def read_from_kafka() -> List[ResponseMetrics]:
    """
    Based on https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
    """
    # Call poll twice. First call will just assign partitions for our
    # consumer without actually returning anything
    consumer_obj = KafkaConsumer(
        KAFKA_TOPIC,
        auto_offset_reset="earliest",
        bootstrap_servers=KAFKA_SERVER,
        client_id="demo-client-1",
        group_id="demo-group",
        security_protocol="SSL",
        ssl_cafile=FILE_SSL_CAFILE,
        ssl_certfile=FILE_SSL_CERTFILE,
        ssl_keyfile=FILE_SSL_KEYFILE,
    )
    data = []
    for _ in range(2):
        raw_msgs = consumer_obj.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                json_value = json.loads(msg.value)
                value = ResponseMetrics(json_value.get('status_code'),
                                        json_value.get('response_time_seconds'),
                                        json_value.get('regexp_pattern_found'),
                                        json_value.get('url')
                                        )
                data.append(value)
    # Commit offsets so we won't get the same messages again
    consumer_obj.commit()
    return data


