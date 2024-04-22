# import os
#
# data_folder = r'C:\Users\Administrator\Desktop\通量数据\CMFD\temp'
#
# # 打印目录中的所有文件，确认文件确实存在
# print("Files in directory:", os.listdir(data_folder))
#
# # 检查特定的文件是否在目录中
# expected_files = [
#     'temp_CMFD_V0106_B-01_03hr_010deg_200301.nc',
#     'temp_CMFD_V0106_B-01_03hr_010deg_200302.nc',
#     # 添加其他预期文件名
# ]
#
# missing_files = [file for file in expected_files if file not in os.listdir(data_folder)]
# if missing_files:
#     print("Missing files:", missing_files)
# else:
#     print("All files are present.")
#检查路径
import os

data_folder = r'C:\Users\Administrator\Desktop\通量数据\CMFD\temp'

# 打印目录中的所有文件路径以确保正确性
for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)
    print(file_path)  # 查看这些打印出的路径是否与预期相符
