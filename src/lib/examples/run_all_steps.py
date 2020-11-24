from lib.common import *
from lib.checker import *
from lib.producer import *
from lib.consumer import *

urls = [
    "https://requests.readthedocs.io/en/master/user/quickstart/",
    "https://requests.readthedocs.io"
]

send_checker_results_to_kafka([checker(url) for url in urls])
data_from_kafka = read_data_from_kafka()
for e in data_from_kafka:
    print("Receiving: {}".format(e))
