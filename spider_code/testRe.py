# @Time: 2020-05-13 13:31
# @Author: skyler 
# @File: testRe.py
# -*- coding: utf-8 -*-


import re

# 创建模式对象

# search, match
pattern = re.compile("AA")  # 此处的'AA'是正则表达式，来验证其他字符串
# m = pattern.search("CBAAAAA")  # 被校验的内容
m = re.search("AA", "CBDFEAA")
print(m)

# findall()
print(re.match('[A-Z]+', 'ASDaGRGRa'))

# sub
print(re.sub('a', 'A', 'abfdgbasger'))

par = '[qwrq"\'f]'
print(par)