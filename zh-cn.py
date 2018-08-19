__author__ = 'mtianyan'
__date__ = '2018/8/20 04:05'

import re

# line = "XXX出生于2001年"
line = "XXX出生于2001/6/1"
# line = "XXX出生于2001-6-1"
# line = "XXX出生于2001-06-01"
# line = "XXX出生于2001-06"

regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}日|[月/-]\d{1,2}|[月/-]$|$))"

match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
