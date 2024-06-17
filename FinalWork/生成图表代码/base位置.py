import matplotlib.pyplot as plt
import pandas as pd

# 设置matplotlib的字体和其他美化选项
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['figure.figsize'] = (10, 6)  # 设置图形的显示大小
plt.rcParams['axes.labelsize'] = 12  # 设置X和Y轴标签的字体大小
plt.rcParams['axes.titlesize'] = 16  # 设置标题的字体大小

# Load data
data = pd.read_excel("统计内容.xlsx")
# Count the occurrences of each 'base位置'
base_counts = data['base位置'].value_counts()

# Create the bar chart
fig, ax = plt.subplots()
base_counts.plot(kind='bar', color='teal', ax=ax)  # 更改颜色为更鲜艳的色彩

# Customize the plot with labels and title
ax.set_xlabel('地点', fontsize=14)
ax.set_ylabel('数量（单位：百）', fontsize=14)
ax.set_title('base位置的统计图表', fontsize=18)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right")  # 旋转X轴标签以避免重叠
# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# # Add gridlines and data labels for clarity
# ax.grid(True, which='both', linestyle='--', linewidth=0.5)  # 添加网格线
# for p in ax.patches:  # 在柱状图上方添加数据标签
#     ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
#                 textcoords='offset points')

plt.tight_layout()  # 调整布局以适应标签
plt.savefig('base位置_美化后.png')  # 保存美化后的图表
plt.show()  # 显示图表
