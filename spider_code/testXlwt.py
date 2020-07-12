# @Time: 2020-05-14 13:56
# @Author: skyler 
# @File: testXlwt.py
# -*- coding: utf-8 -*-


import xlwt, os


workbook = xlwt.Workbook(encoding='utf-8')   # 创建workboook对象
worksheet = workbook.add_sheet('sheet1')    # 创建一个sheet
worksheet.write(10, 0, 'hello')      # 写入数据，第一个参数 行， 第二个参数 列

# 九九乘法表
for i in range(9):
    for j in range(i + 1):
        worksheet.write(i, j, f'{i + 1} * {j + 1} = {(i + 1) * (j + 1)}')
workbook.save('test.xls')
print(os.getcwd())