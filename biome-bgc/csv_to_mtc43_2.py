import os

def convert_csv_to_txt(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):  # 检查文件扩展名是否为.csv
            csv_file_path = os.path.join(directory, filename)
            txt_file_path = os.path.join(directory, filename[:-4] + '.mtc43')  # 构建.txt文件的路径
            with open(csv_file_path, 'r', encoding='utf-8') as csv_file, \
                 open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                for line in csv_file:
                    txt_file.write(line.replace(',', ' '))  # 将逗号替换为空白字符

# 调用函数并传入包含CSV文件的目录路径
convert_csv_to_txt(r'C:\Users\Administrator\Desktop\fluxdata\finishtemp')