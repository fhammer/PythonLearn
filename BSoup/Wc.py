#!/usr/bin/python
# -*-coding:utf-8-*-
from PIL import Image
from scipy.ndimage import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# 从文本中读取文本先
of = open("./doc.txt", encoding='utf-8')
lstr = of.read()
print(lstr)
of.close()
# 图片设置
img = Image.open("./head.jpg")
width, height = img.size
diao_img = imread("./head.jpg")
'''
Arial.ttf字体文件可以网上下载background_color:背景颜色mask：
背景图片stopwordsmax_font_size：字体最大大小
'''
wc = WordCloud('./Arial.ttf',
               width=width,
               height=height,
               background_color="white",
               mask=diao_img,
               font_step=3,
               max_font_size=30,
               random_state=False,
               prefer_horizontal=0.9)
wc.generate(lstr)
# 提取背景图片的颜色
img_cl = ImageColorGenerator(diao_img)
# 显示图片
plt.imshow(wc)
plt.axis("off")
# 绘制
plt.figure()
plt.imshow(wc.recolor(color_func=img_cl))
plt.axis("off")
# 使用背景图片的颜色制作图片
plt.figure()
plt.imshow(diao_img, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# save img
wc.to_file("./diao_words.png")
