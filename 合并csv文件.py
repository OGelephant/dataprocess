import pandas as pd
import os

# 设置CSV文件所在的文件夹路径
folder_path = r'C:\Users\Administrator\Desktop\fluxdata\CMFD\prec\HB'

# 创建一个空的DataFrame用来存放合并后的数据
combined_csv = pd.DataFrame()

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, file_name)
        # 读取CSV文件
        df = pd.read_csv(file_path)
        # 将读取的数据追加到combined_csv DataFrame中
        combined_csv = pd.concat([combined_csv, df], ignore_index=True)

# 将合并后的数据存储到新的CSV文件中
combined_csv.to_csv(r'C:\Users\Administrator\Desktop\fluxdata\CMFD\prec\HB\HBSpreccombined_csv.csv', index=False)

print("文件已合并并保存")
