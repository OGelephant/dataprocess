import os
import pandas as pd

# 指定要遍历的目录
directory = r'C:\Users\Administrator\Desktop\fluxdata\finishtemp'

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    # 检查文件扩展名是否为.csv
    if filename.endswith('.csv'):
        # 构造完整的文件路径
        file_path = os.path.join(directory, filename)

        # 使用pandas读取csv文件
        df = pd.read_csv(file_path)

        # 构造新的文本文件路径，将.csv扩展名改为.txt
        text_file_path = os.path.splitext(file_path)[0] + '.mtc43'

        # 将DataFrame写入文本文件
        df.to_csv(text_file_path, index=False, header=True)