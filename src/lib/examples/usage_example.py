"""
Run all steps sequentially to demonstrate usage example.
"""
from lib.producer import *
from lib.consumer import *
from loguru import logger

urls = [
    "https://requests.readthedocs.io/en/master/user/quickstart/",
    "https://requests.readthedocs.io"
]

for url in urls:
    metrics = measure_metrics(url)
    logger.info("Received metrics: {}".format(metrics))
    send_data_to_kafka(metrics)
    logger.info(".. sent to Kafka service")
data_from_kafka = get_data_from_kafka()
for e in data_from_kafka:
    logger.info("Received from Kafka service: {}".format(e))
