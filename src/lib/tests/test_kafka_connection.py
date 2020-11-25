from lib.settings import *
from kafka import KafkaConsumer, KafkaProducer, errors


def test_kafka_connection():
    try:
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
        r = consumer.topics()
        assert r == set(['metrics'])
    except errors.NoBrokersAvailable as e:
        raise errors.NoBrokersAvailable("Kafka connection error") from e


