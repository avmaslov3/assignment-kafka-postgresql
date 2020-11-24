"""
Common across modules data and functions
"""
from collections import namedtuple

CheckerResults = namedtuple('ResponseMetrics',
                            ['status_code', 'response_time_seconds',
                             'web_page_text'],
                            defaults=[None, None, None])
