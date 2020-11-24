from lib.common import *
from lib.checker import *
from lib.producer import *


r = checker("https://requests.readthedocs.io/en/master/user/quickstart/")

send_checker_results_to_kafka([r])
