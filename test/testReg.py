# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/1/17 0017 16:20'

import re

line = "XXX出生于2001年6月1日"
line = "XXX出生于2001/6/1"
line = "XXX出生于2001-6-1"
# line = "XXX出生于2001-06-01"
# line = "XXX出生于2001-06"

regex_str5 = ".*?(\d+)年"
regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}日|[月/-]\d{1,2}|[月/-]$|$))"

match_obj = re.match(regex_str, line)
if match_obj:
    print (match_obj.group(1))
