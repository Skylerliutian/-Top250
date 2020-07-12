# @Time: 2020-05-14 21:48
# @Author: skyler 
# @File: testSqlite.py
# -*- coding: utf-8 -*-

import sqlite3


# 1. 创建数据库
conn = sqlite3.connect('test.db')   # 打开或创建数据库文件
print('Opened database successfully')
c = conn.cursor()   # 获取游标

# 2. 创建数据表
# conn = sqlite3.connect('test.db')   # 打开或创建数据库文件
# print('Opened database successfully')
# c = conn.cursor()   # 获取游标
# create_sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
#
# '''
# c.execute(create_sql)  # 执行sql语句
# conn.commit()   # 提交数据库操作
# conn.close()    # 关闭数据库连接
# print('Table created')

# 3. 插入数据
# insert_sql_1 = '''insert into company values (1, 'Skyler', 23, 'A318/42 Page St Banksmedow', 30000);
# '''
# insert_sql_2 = '''insert into company values (2, 'Ruby', 23, 'A318/42 Page St Banksmedow', 30000);
# '''
# c.execute(insert_sql_1)  # 执行sql语句
# c.execute(insert_sql_2)
# conn.commit()   # 提交数据库操作
# conn.close()    # 关闭数据库连接
# print('Successfully inserted')


# 4. 查询数据
sel_sql = 'select id, name, address, salary from company'
cursor = c.execute(sel_sql)     # 执行sql语句
print(cursor)
for row in cursor:
    print('id = ', row[0])
    print('name = ', row[1])
    print('address = ', row[2])
    print('salary = ', row[3], '\n')


conn.commit()   # 提交数据库操作
conn.close()    # 关闭数据库连接