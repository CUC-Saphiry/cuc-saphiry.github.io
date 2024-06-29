import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from PIL import Image

# 读取Excel文件
file_path = '统计内容.xlsx'
data = pd.read_excel(file_path)

# 获取岗位名称列
job_titles = data['岗位名称']

jieba.add_word('唯品会')
jieba.add_word('路虎')
jieba.add_word('讯飞')
jieba.add_word('汤臣倍健')
jieba.add_word('新媒体')

# 定义要去掉的特定词
stop_words = ["\t", " ","-","（","）", "_","/","•","|","部","&",'丨',"进化","方向"]

# 对岗位名称进行分词，并过滤掉特定词和停用词
words = jieba.cut(' '.join(job_titles.astype(str)))
filtered_words = [word for word in words if word not in stop_words]

# 计算词频
word_freq = Counter(filtered_words)

# 取词频前50
word_freq_top50 = word_freq.most_common(50)

# 打印词频前50
print(word_freq_top50)

# 构建词频前50的字典
word_freq_dict = dict(word_freq_top50)

# 加载图像作为遮罩
mask = np.array(Image.open(r"data/star.png"))

# 定义颜色函数，使颜色在一个蓝色的色系中变化
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"hsl(210, 100%, {int(100.0 * float(random_state.randint(60, 120)) / 255.0)}%)"

# 生成词云图
wordcloud = WordCloud(font_path='simhei.ttf',
                      width=800,
                      height=400,
                      background_color='white', mask=mask,color_func=blue_color_func).generate_from_frequencies(word_freq_dict)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
