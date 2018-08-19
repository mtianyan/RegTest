import re

__author__ = 'mtianyan'
__date__ = '2018/8/20 03:41'

"""
默认为贪婪模式: 会去根据字符串匹配最大的长度 
Output: mm

原因: 正则表达式扫描字符串是从右向左匹配(反向), 遇到第一个m，中间的任意次可以是0次，因此匹配到mm(全怪从右开始)
括号括起来我们需要的字符串.也就是只提取这一部分。
"""
line = "moooommtianyan123"
# m前面任意重复次字符,m和后一个m中间任意重复字符，后面也任意重复次字符。
regex_str2 = ".*(m.*m).*"
match_obj = re.match(regex_str2, line)
if match_obj:
    # 只取第一个括号的东西(子串)
    print(match_obj.group(1))

"""
输出moooomm
使用?修饰*使得从第一个m的匹配是从左开始匹配的，但第二个m还是一种贪婪的匹配(从右往左的)
"""
regex_str3 = ".*?(m.*m).*"
match_obj = re.match(regex_str3, line)
if match_obj:
    print(match_obj.group(1))

"""
使用?使他从左边开始但是右边还是贪婪模式匹配
在第二个m前也加问号,让它也从左起开始。找这样的条件的m，不要继续向后贪婪
"""
regex_str4 = ".*?(m.*?m).*"
match_obj = re.match(regex_str4, line)
if match_obj:
    print(match_obj.group(1))
