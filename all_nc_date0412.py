from netCDF4 import Dataset
import numpy as np
import pandas as pd
import os

# 设置包含nc文件的文件夹路径
folder_path = r'F:\jssjdata\tmn'

# 获取文件夹中所有的nc文件
nc_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.nc')]
print(nc_files)

# 遍历所有的nc文件
for file in nc_files:
    # 读取数据
    data = Dataset(file)
    print(f'Opened file: {file}')

    # 取出经纬度变量
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    # 设置自己目标站点的经纬度
    lat_T = 42.4
    lon_T = 128.4667

    # 对经纬度列表进行做差并平方（避免负数）
    sq_lat = (lat - lat_T) ** 2
    sq_lon = (lon - lon_T) ** 2

    # 找出差值最小的点（也就是距离目标站点最近的点）
    min_lat_idx = sq_lat.argmin()
    min_lon_idx = sq_lon.argmin()

    # 提取出我们需要的气温变量
    tmn = data.variables['tmn'][:]
    # 获取时间变量及其单位
    time_var = data.variables['time']
    time_data = time_var[:]


    # 由于tmn是一个三维数组，我们需要提取出距离目标站点最近的点的数据
    # 假设tmn的第一个维度是时间，第二个维度是纬度，第三个维度是经度
    target_tmn = tmn[:, min_lat_idx, min_lon_idx]

    # 创建一个包含时间、气温的DataFrame
    df = pd.DataFrame({'Time': time_data, 'Temperature': target_tmn})

    # 为输出文件名添加文件名部分，以便区分不同文件的数据
    output_filename = f'CBStmn_{os.path.basename(file).replace(".nc", ".csv")}'
    output_file = os.path.join(folder_path, output_filename)

    # 保存DataFrame到csv文件
    df.to_csv(output_file, index=False)

    # 打印完成信息
    print(f'Temperature data has been saved to file: {output_file}')