from netCDF4 import Dataset
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# 读取数据
data = Dataset(r'C:\Users\Administrator\Desktop\Data_forcing_01dy_010deg\Data_forcing_01dy_010deg\prec_CMFD_V0106_B-01_01dy_010deg_200801-200812.nc')

# 取出经纬度变量
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]

# 设置自己目标站点的经纬度
lat_T = 42.40
lon_T = 128.4667

# 对经纬度列表进行做差并平方（避免负数）
sq_lat = (lat - lat_T) ** 2
sq_lon = (lon - lon_T) ** 2

# 找出差值最小的点（也就是距离目标站点最近的点）
min_lat_idx = sq_lat.argmin()
min_lon_idx = sq_lon.argmin()

# 提取出我们需要的降水量变量
prec = data.variables['prec'][:]

# 由于prec是一个三维数组，我们需要提取出距离目标站点最近的点的数据
# 假设prec的第一个维度是时间，第二个维度是纬度，第三个维度是经度
target_prec = prec[:, min_lat_idx, min_lon_idx]

# 读取时间数据并转换为datetime对象
time_data = data.variables['time'][:]
date_format = '%Y-%m-%d %H:%M:%S'
time_units = data.variables['time'].units  # 获取时间单位

# 如果时间单位是'days since 1980-01-01 00:00:00'，则需要转换时间
if 'days since' in time_units:
    time_data = nc.num2date(time_data, time_units)

# 创建一个包含时间、降水量的DataFrame
df = pd.DataFrame({'Time': time_data, 'Precipitation': target_prec})

# 保存DataFrame到csv文件
output_file = 'CBSprecipitation2008.csv'
df.to_csv(output_file, index=False)

# 打印完成信息
print(f'降水数据已保存到文件：{output_file}')