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
    send_checker_result_to_kafka(measure_url_metrics(url))
data_from_kafka = get_data_from_kafka()
for e in data_from_kafka:
    logger.info("Receiving: {}".format(e))
