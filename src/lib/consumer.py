"""
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
"""
from lib.settings import *
from kafka import KafkaConsumer
from loguru import logger
import time


@logger.catch()
def get_data_from_kafka():
    """
    Based on https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
    """
    # Call poll twice. First call will just assign partitions for our
    # consumer without actually returning anything
    consumer = KafkaConsumer(
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
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                data.append(msg.value)
    # Commit offsets so we won't get the same messages again
    consumer.commit()
    return data


@logger.catch()
def consumer(sleep_interval: float = 1.0):
    try:
        while True:
            data_kafka = get_data_from_kafka()
            if len(data_kafka) > 0:
                logger.info(f"Received data from Kafka. len(data) ="
                            f" {len(data_kafka)}")
            else:
                logger.info("Kafka topic is empty")
            time.sleep(sleep_interval)
    except KeyboardInterrupt:
        print("Stop consumer!")
