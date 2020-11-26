"""
Common across modules data and functions
"""
from collections import namedtuple
import glob
import os

ResponseMetrics = namedtuple('ResponseMetrics',
                             ['status_code',
                              'response_time_seconds',
                              'web_page_text',
                              'url'],
                             defaults=[None]*4)

AccessFilesPaths = namedtuple('AccessFilesPaths', ['ca_file', 'cert_file',
                                                   'key_file'])


