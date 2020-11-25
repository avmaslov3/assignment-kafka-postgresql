"""
Run all steps sequentially to demonstrate usage example.
"""
from lib.producer import *
from lib.consumer import *
from lib.database import *
from loguru import logger


def test_write_to_table():
    """
    Write dummy data to PostgreSQL and read back
    """
    write_message_to_db(ResponseMetrics(200, 15, None, 'https'))
    res = request_db("SELECT * FROM METRICS;")[-1]
    logger.info(res)


if 1 == 0:
    # Drop and re-create table optionally
    drop_if_exist_and_create_table()

urls = ["https://requests.readthedocs.io"]


for url in urls:
    metrics = measure_metrics(url)
    logger.info("Received metrics: {}".format(metrics))
    send_data_to_kafka(metrics)
    logger.info(".. message was sent to Kafka service")
data_from_kafka = get_data_from_kafka()
for message in data_from_kafka:
    logger.info("Received from Kafka service: {}".format(message))
    write_message_to_db(message)
    logger.info("..Saved into database")

test_query = request_db("SELECT * FROM METRICS;")
logger.info("SELECT * FROM METRICS == {}".format(test_query))


