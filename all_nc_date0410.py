from netCDF4 import Dataset, num2date
import numpy as np
import pandas as pd
import os


# 设置包含nc文件的文件夹路径
folder_path = r'C:\Users\Administrator\Desktop\Data_forcing_01dy_010deg\prec'

# 获取文件夹中所有的nc文件
nc_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.nc')]

# 遍历所有的nc文件
for file in nc_files:
    # 读取数据
    data = Dataset(file)

    # 取出经纬度变量
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]

    # 设置自己目标站点的经纬度
    lat_T = 37.516667
    lon_T = 101.316667

    # 对经纬度列表进行做差并平方（避免负数）
    sq_lat = (lat - lat_T) ** 2
    sq_lon = (lon - lon_T) ** 2

    # 找出差值最小的点（也就是距离目标站点最近的点）
    min_lat_idx = sq_lat.argmin()
    min_lon_idx = sq_lon.argmin()

    # 提取出我们需要的降水量变量
    prec = data.variables['prec'][:]


    # 获取时间变量及其单位
    time_var = data.variables['time']
    time_data = time_var[:]

    # 获取时间单位
    time_units = time_var.units
    # 如果时间单位是'days since 1980-01-01 00:00:00'，则需要转换时间
    if 'days since' in time_units:
        time_data = num2date(time_data, time_units)

    # 由于prec是一个三维数组，我们需要提取出距离目标站点最近的点的数据
    # 假设prec的第一个维度是时间，第二个维度是纬度，第三个维度是经度
    target_prec = prec[:, min_lat_idx, min_lon_idx]

    # 读取时间数据并转换为datetime对象
    time_data = num2date(data.variables['time'][:], data.variables['time'].units)

    # 如果时间单位是'days since 1980-01-01 00:00:00'，则需要转换时间
    if 'days since' in time_units:
        time_data = nc.num2date(time_data, time_units)

    # 创建一个包含时间、降水量的DataFrame
    df = pd.DataFrame({'Time': time_data, 'Precipitation': target_prec})

    # 为输出文件名添加文件名部分，以便区分不同文件的数据
    output_filename = f'HBprecipitation_{os.path.basename(file).replace(".nc", ".csv")}'
    output_file = os.path.join(folder_path, output_filename)

    # 保存DataFrame到csv文件
    df.to_csv(output_file, index=False)

    # 打印完成信息
    print(f'降水数据已保存到文件：{output_file}')