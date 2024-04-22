from netCDF4 import Dataset
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# 读取数据
data  = Dataset(r'C:\Users\Administrator\Desktop\prec_200301-200312.nc')

# 取出经纬度变量
lat = data.variables['lat'][:]
# print(data.variables)
lon = data.variables['lon'][:]

#设置自己目标站点的经纬度
lat_T = 42.40
lon_T = 128.4667

# 对经纬度列表进行做差并平方（避免负数）
sq_lat = (lat - lat_T)**2
sq_lon = (lon - lon_T)**2

# 找出差值最小的点下表（也就是距离目标站点最近的点）
min_lat = sq_lat.argmin()
min_lon = sq_lon.argmin()

# 提取出我们需要的降水量变量
prec = data.variables['prec']

# 创建一个新的数据框
time_data = data.variables['time'][:]



df.to_csv("jiangshui")