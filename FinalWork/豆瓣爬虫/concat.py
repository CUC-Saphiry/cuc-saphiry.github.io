# 定义要合并的文件数量和基本文件名
num_files = 50
base_filename = '{}.txt'  # 替换 /path/to/files/ 为文件所在的路径

# 打开一个新文件用于写入合并后的内容
with open('merged.txt', 'w', encoding='utf-8') as outfile:  # 替换 /path/to/files/merged.txt 为最终文件的路径和文件名
    # 循环处理每个文件
    for i in range(1, num_files + 1):
        filename = base_filename.format(i)
        try:
            with open(filename, 'r', encoding='utf-8') as infile:
                contents = infile.read()
                outfile.write(contents + '\n')  # 在文件内容之间添加换行符以分隔
        except FileNotFoundError:
            print(f"File {filename} not found. Skipping...")

print("Files have been successfully merged into merged.txt")
