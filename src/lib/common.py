"""
Common across modules data and functions
"""
from collections import namedtuple

CheckerResults = namedtuple('ResponseMetrics',
                            ['status_code',
                             'response_time_seconds',
                             'web_page_text',
                             'url'],
                            defaults=[None]*4)
