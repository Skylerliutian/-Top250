# @Time: 2020-05-12 11:00
# @Author: skyler 
# @File: testBs4.py
# -*- coding: utf-8 -*-

'''
BeautifulSoup4将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是
python对象，所有对象可以归纳为4种：

- Tag
- NavigableString
- BeautifulSoup
- Comment
'''
from bs4 import BeautifulSoup

file = open('./baidu.html', 'rb')
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, 'html.parser')

# 1.tag 标签及其内容, 拿到所找到的第一个标签
# print(bs.title)
# print(bs.meta)
# print(bs.a)
#
#
# # 2. NavigableString 标签里的内容
# print(bs.title.string)
# print(bs.a.attrs)  # 一个标签里所有的属性
#
# # 3. BeautifulSoup, 表示整个文档
# print(bs)
#
# # 4. Comment 是一个特殊的NavigableString, 输出的内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))


# ---------------------------------

# 文档的遍历
# print(bs.head.contents[1])


# 文档的搜索

# 1. find_all()
# 字符串过滤：就差着与字符串完全匹配的内容
# t_list = bs.find_all('a')  # 找到所有的 'a' 标签, 可以加多个标签表示 and
# print(t_list)


import re
# # 2. 正则表达式
# t_list = bs.find_all(re.compile('a'))
# print(t_list)


# 3. 方法：传入一个函数(方法), 根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr('name')
#
# t_list = bs.find_all(name_is_exists)
# print(t_list)


# 2.kwargs 参数
# t_list = bs.find_all(id='head')
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href='http://news.baidu.com')
# print(t_list)


# 3.text 参数
# l = ['hao123', '贴吧', '地图', 'wdw']
# t_list = bs.find_all(text = l)
# t_list = bs.find_all(text=re.compile('\d')) # 正则表达式来查找包含特定文本的内容（标签里的字符串）
# for i in t_list:
#     print(i)
# print(t_list)

# 4.limit 参数
t_list = bs.find_all('a', limit=3)
print(t_list)

# 5.css选择器
# t_list = bs.select('title')  # 通过标签来查找
# t_list = bs.select('.mnav')  # . 表示通过类名来查找
# t_list = bs.select('#u1')  # 通过id来查找
# t_list= bs.select('a[class = "toindex"]')  # 通过属性来查找
# t_list = bs.select('head > title')  # head标签下的 title, 通过子标签来查找
t_list = bs.select(".bri")
print(t_list)