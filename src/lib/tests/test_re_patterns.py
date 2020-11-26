from lib.common import *
import requests


def test_re_patterns():
    assert check_re_pattern_page_text("ewdhjei 983 ", r"[0-9]{3,5}")
    assert not check_re_pattern_page_text("ewdhjei 98w ww ", r"[0-9]{3,5}")
    web_page_text = requests.get("https://docs.python.org/3/library/re.html").text
    assert check_re_pattern_page_text("qs wsw q aaaaaa asqw sws ", r"[a]{5}")
    assert check_re_pattern_page_text(web_page_text, r"[a]{6}")
    assert not check_re_pattern_page_text(web_page_text, r"[a]{7}")
