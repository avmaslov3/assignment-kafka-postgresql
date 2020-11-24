"""
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
"""
from src.settings import *
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    auto_offset_reset="earliest",
    bootstrap_servers=KAFKA_SERVER,
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="../ca.pem",
    ssl_certfile="../service.cert",
    ssl_keyfile="../service.key",
)

# Call poll twice. First call will just assign partitions for our
# consumer without actually returning anything

for _ in range(2):
    raw_msgs = consumer.poll(timeout_ms=1000)
    for tp, msgs in raw_msgs.items():
        for msg in msgs:
            print("Received: {}".format(msg.value))


# Commit offsets so we won't get the same messages again
consumer.commit()