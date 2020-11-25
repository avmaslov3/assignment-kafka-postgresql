"""
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
"""
from lib.settings import *
from kafka import KafkaConsumer
from loguru import logger


@logger.catch()
def read_data_from_kafka():
    """
    Based on https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
    """
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

    # Call poll twice. First call will just assign partitions for our
    # consumer without actually returning anything
    for _ in range(2):
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                logger.info("Receiving to consumer: {}".format(msg))
                yield msg.value

    # Commit offsets so we won't get the same messages again
    consumer.commit()


