import pandas as pd
import re

import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# 设置读取Excel文件的路径
file_path = '统计内容.xlsx'

# 读取Excel文件
data = pd.read_excel(file_path)

# 针对“岗位职责”列进行预处理
# 替换换行符、多余的空格以及标点符号
data['岗位职责'] = data['岗位职责'].astype(str).apply(lambda x: re.sub(r'[\n\t；。、|•]', ' ', x))  # 替换特定标点和换行符为一个空格
data['岗位职责'] = data['岗位职责'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())  # 替换多余的空格，并去除字符串首尾的空格

# 输出预处理后的数据，查看效果
print(data['岗位职责'].head())


# 将所有的文本行拼接成一个长字符串
combined_text = ' '.join(data['岗位职责'])




# 设置matplotlib的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



# 获取岗位要求列，并删除换行符
data['岗位职责'] = data['岗位职责'].astype(str).str.replace('\n', ' ', regex=False).replace('；', ' ', regex=False).replace('。', ' ', regex=False)

# 获取岗位名称列
job_titles = data['岗位要求']

jieba.add_word('唯品会')
jieba.add_word('路虎')
jieba.add_word('讯飞')
jieba.add_word('汤臣倍健')
jieba.add_word('新媒体')
jieba.add_word('有能力')
jieba.add_word('有经验')
jieba.add_word('相关经验')
jieba.add_word('有经验')
jieba.add_word('3天')
jieba.add_word('4天')
jieba.add_word('6个月')
jieba.add_word('到岗')
jieba.add_word('加分')
jieba.add_word('3个月')
jieba.add_word('三个月')
jieba.add_word('5个月')
jieba.add_word('5天')
jieba.add_word('实习经验')
jieba.add_word('运营经验')
jieba.add_word('相关经验')
jieba.add_word('研究生以上学历')
jieba.add_word('本科以上学历')
jieba.add_word('研究生以上学历')
jieba.add_word('用户社群')
jieba.add_word('平台账号')
jieba.add_word('分析数据')

# 定义要去掉的特定词
stop_words = ["\t", " ","-","（","）", "_","/","•","|","部","&",'丨',"进化","方向","，",'；','。','、',"的","等","有","和","对","及","或","能","者","可","较","届",".","能","以上","能","能","能","能","能","能","能","能","强","能","不","能","相关","月","考虑","具有","能","1","2","3","一定","能","4","并","能","在","好","能","至少","与","能","能","：","能","能","能","能","能","能","能"]

# 对岗位名称进行分词，并过滤掉特定词和停用词
words = jieba.cut(combined_text)
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
