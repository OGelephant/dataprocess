from netCDF4 import Dataset
import numpy as np
import pandas as pd
from datetime import datetime

# 读取数据
data = Dataset(r'C:\Users\Administrator\Desktop\prec_200301-200312.nc')

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

# 读取时间数据并转换为datetime对象
time_data = data.variables['time'][:]

# 获取时间单位
time_units = data.variables['time'].units

# 如果时间单位是'days since 1980-01-01 00:00:00'，则需要转换时间
if 'days since' in time_units:
    # 转换时间单位为datetime对象
    time_objects = nc.num2date(time_data, time_units)
    # 将datetime对象转换为日期字符串
    time_strings = [datetime.strftime(d, '%Y-%m-%d') for d in time_objects]
else:
    # 如果时间单位不是'days since'，则直接使用时间数据
    time_strings = [str(t) for t in time_data]

# 创建一个包含日期字符串和降水量的DataFrame
df = pd.DataFrame({'Date': time_strings, 'Precipitation': prec[:, min_lat_idx, min_lon_idx]})

# 保存DataFrame到csv文件
output_file = 'precipitation_data1.csv'
df.to_csv(output_file, index=False)

# 打印完成信息
print(f'降水数据已保存到文件：{output_file}')