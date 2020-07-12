# @Time: 2020-05-20 08:51
# @Author: skyler 
# @File: testWordcloud.py
# -*- coding: utf-8 -*-

import jieba    # 分词 -- 一个句子分成好几个词
from matplotlib import pyplot as plt
from wordcloud import WordCloud             # 词云
from PIL import Image                       # 图片处理
import numpy as np
import sqlite3

# 准备词云所需的文字
conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ''
for item in data:
    text += item[0]
cur.close()
conn.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)

img = Image.open('./tree.jpg')
img_array = np.array(img)       # 将图片转换为数组

wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='STHeiti Medium.ttc',    # 字体所在位置, cmd+space search fonts
)

wc.generate_from_text(string)


# 绘制图片
fig = plt.figure()
plt.imshow(wc)
plt.axis('off')     # 是否显示坐标轴
# plt.show(dpi=600)
plt.savefig('word.jpg', dpi=500)