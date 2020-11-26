"""
Common across modules data and functions.
"""
from collections import namedtuple
import re

ResponseMetrics = namedtuple('ResponseMetrics',
                             ['status_code',
                              'response_time_seconds',
                              'regexp_pattern_found',
                              'url'],
                             defaults=[None]*4)

AccessFilesPaths = namedtuple('AccessFilesPaths', ['ca_file', 'cert_file',
                                                   'key_file'])


def check_re_pattern_page_text(text: str,
                               regexp_pattern: str = r"") -> bool:
    p = re.compile(regexp_pattern)
    return bool(p.search(text))

