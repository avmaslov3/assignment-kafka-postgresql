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


def paths_to_access_files(dir_path: str) -> AccessFilesPaths:
    """
    Function is needed if we would need to pass access keys paths using
    command line arguments.
    Return list of paths to files
    - service.cert
    - service.key
    - ca.pem
    """
    ca_file = glob.glob(os.path.normpath(dir_path) + "/ca.pem")
    cert_file = glob.glob(os.path.normpath(dir_path) + "/service.cert")
    key_file = glob.glob(os.path.normpath(dir_path) + "/service.key")
    try:
        assert len(cert_file) == 1
        assert len(key_file) == 1
        assert len(ca_file) == 1
    except AssertionError as e:
        raise AssertionError("Not all access files are found in {}".format(
            os.path.abspath(dir_path)))
    return AccessFilesPaths(ca_file[0], cert_file[0], key_file[0])
