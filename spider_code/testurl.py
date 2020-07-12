# @Time: 2020-05-11 17:55
# @Author: skyler 
# @File: testurl.py
# -*- coding: utf-8 -*-

from urllib import request, parse, error
import socket


# 获取一个get请求
# res = request.urlopen('http://www.baidu.com/')
# print(res.read().decode('utf-8'))


# 模拟浏览器访问，避免反爬虫监测
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)\
#               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
# resq = request.Request('https://movie.douban.com/top250?start=25&filter=', headers=headers)
# response = request.urlopen(resq)
# print(response.read().decode('utf-8'))


#获取一个post请求
# data = bytes(parse.urlencode({'hello': 'world'}), encoding='utf-8')
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))


#超时检测
# try:
#     response = request.urlopen('http://httpbin.org/get', timeout=0.01)
#     print(response.read().decode('utf-8'))
# except socket.timeout as e:
#     print("time out!")

# response = request.urlopen("http://www.baidu.com/")
# print(response.getheaders())
# print(response.getheader('Set-Cookie'))
