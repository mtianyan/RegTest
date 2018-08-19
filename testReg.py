# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/1/17 0017 16:20'

import re

line = "mtianyan123"

"""
定义正则表达式的字符串模式
^m代表以m开头；.代表任意字符；* 代表前面字符可以重复任意遍
3$代表以3为结尾
"""
regex_str1 = "^m.*3$"

"""
两个参数: 定义的字符串，以及我们要检验的字符串
"""
if re.match(regex_str1, line):
    print("yes")

