# -*- coding:utf-8 -*-
# @Time: 2020-05-10 21:50
# @Author: skyler
# @File: spider.py

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re
from urllib import request, error  # 指定URL，获取网页数据
import xlwt
import pandas as pd
import sqlite3


def main():
    # 1.爬取网页
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    saveName = 'Top250MoviesOndouban'
    dbName = 'movie.db'
    # 3.保存数据
    saveData(datalist, saveName)
    viaSqlite(datalist, dbName)
    # viaCsv(datalist, saveName)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(10):  # 调用获取页面信息的函数，10次(每页25条数据)
        url = baseurl + str(25*i)
        html = askURL(url)

        # 2.逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_='item'):   # 查找符合要求的字符串，组成列表
            # (标签-在html源代码中查询 , 类别)  搜索同时满足这两个条件的内容
            # print(item)     # 测试，查找电影item全部信息
            # print('-----------------------')
            data = []  # 保存一部电影的所有信息
            item = str(item)

            # 影片名称
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]      # 添加中文名称
                data.append(ctitle)
                otitle = titles[1].replace('/', '')     # 添加别名
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')    # 别名留空，因为最后要生成文件 不能为空

            # 影片评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            # 影片评价人数
            judgeNum = re.findall(findPeople, item)[0]
            data.append(judgeNum)

            # 影片概述
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', '')   # 去掉句号
                data.append(inq)
            else:
                data.append(' ')

            # 影片内容
            bd = re.findall(findBd, item)[0].strip()
            bd = re.sub(r'<br(\s+)?/>[\s\n]+', '   ', bd)   # 去掉 <br/>
            bd = re.sub('/', '', bd)                    # 去掉 /
            data.append(bd)

            # 影片详情链接
            link = re.findall(findLink, item)[0]  # re库通过正则表达式来查找指定字符串
            data.append(link)  # 添加链接
            # 图片链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片链接

            datalist.append(data)   # 整个影片的所有信息
    return datalist


# 得到一个指定URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，像豆瓣服务器发送消息
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)\
                  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器(本质上是告诉浏览器我们可以接受什么水平的文件内容)
    req = request.Request(url, headers=header)
    html = ''
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


# 保存数据, 保存到excel中
def saveData(datalist, name):
    print('--------Saving process begin--------')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workboook对象
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)  # 创建一个sheet
    column = ('影片中文名', '影片别名', '评分', '评价人数', '概况', '相关信息','电影详情链接', '图片链接')
    attrNum = len(column)
    for i in range(attrNum):
        sheet.write(0, i, column[i])    # 写入列名
    for i in range(250):    # 写入数据
        print(f'No.{i + 1} is writing......')
        for j in range(attrNum):
            sheet.write(i + 1, j, datalist[i][j])   # 写入数据
    print('--------Saving successful--------')
    book.save(name + '.xls')   # 保存


# 保存数据, 保存成为csv文件
def viaCsv(datalist, name):
    print('--------Saving process begin--------')
    column = ['影片中文名', '影片别名', '评分', '评价人数', '概况', '相关信息', '电影详情链接', '图片链接']
    dataframe = pd.DataFrame(datalist, columns=column)
    print('--------Saving successful--------')
    dataframe.to_csv(name + '.csv')


def viaSqlite(datalist, dbName):
    init_db(dbName)
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index != 2 and index != 3:
                data[index] = '"' + data[index].strip() + '"'
        sql = '''insert into movie250 (cname, ename, score, rated, introduction, info, info_link, pic_link) 
        values (%s)''' % (','.join(data))

        cursor.execute(sql)
        conn.commit()
    conn.close()


def init_db(dbName):
    sql = '''
        create table movie250 (
            id integer  primary key autoincrement,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text,
            info_link text,
            pic_link text
        )
    '''    # 创建数据表
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':

    # 影片链接 正则
    findLink = re.compile(r'<a href="(.*)">')     # 创建正则表达式对象，表示规则，字符串的模式
    # 影片图片 正则
    findImgSrc = re.compile(r'<.*src="(.*?)" .*/>', re.S)  # re.S . 同时匹配换行符
    # 影片片名 正则
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    # 影片评分 正则
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    # 影评人数 正则
    findPeople = re.compile(r'<span>(\d*)人评价</span>')
    # 概况 正则
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    # 找到影片的相关内容
    findBd = re.compile('<p class="">(.*?)</p>', re.S)

    # 初始化 数据库
    # init_db('movies250.db')

    # main()
    people = 'Skyler'
    p = ['dwdw', 'dwdwd', 'dwdwdw']
    s = 'Who is the most handsome and charming guy?  %s' % ','.join(p)
    print(s)

