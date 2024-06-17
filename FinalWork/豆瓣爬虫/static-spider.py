import requests
from bs4 import BeautifulSoup
import tkinter as tk
from ttkbootstrap import Style

# 定义一个函数来处理每个链接
def process_url(url, file_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 清空原文档内容
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("")

    # 以追加的方式写入文档
    comments = soup.find_all('h1')
    for comment in comments:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(comment.text.strip())
            f.write("\n")

    comments = soup.find_all('div', class_="rich-content")
    for comment in comments:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(comment.text.strip())
            f.write("\n")
            f.write("【评论】")
            f.write("\n")

    comments = soup.find_all('span', class_='short')
    for comment in comments:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(comment.text.strip())
            f.write("\n")

# 中心化窗口的函数
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# 爬取完成后显示提示窗口的函数
def show_completion_message():
    root = tk.Tk()
    style = Style(theme='vapor')  # 您可以选择任何您喜欢的主题
    label = tk.Label(root, text="爬取完成", padx=20, pady=20)
    label.pack()
    center_window(root)
    root.mainloop()

# 从文本文件中读取链接
with open('links.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f]

# 处理每个链接
for i, url in enumerate(urls, start=1):
    file_name = f"{i}.txt"
    process_url(url, file_name)

# 爬取完成后显示提示窗口
show_completion_message()
