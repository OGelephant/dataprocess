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
lat_T = 27.697817
lon_T = 85.329806

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
# start_date = print(data.variables['time'].units[11:-9])
start_date = datetime(1900, 1, 1)

# 计算每个时间戳对应的日期时间
# 首先，我们需要将每个小时数转换为天数，然后将其转换为 timedelta 对象
# 因为 1 天有 24 小时，所以我们除以 24
time_deltas = [time / 24 for time in time_data]

# 然后，我们将每个 timedelta 对象添加到起始日期上
#timedelta(days=td) 是 datetime 模块中的一个函数，
# 它创建一个时间差对象，表示 td 天的时间长度。这里的 td 来自前面计算得到的 time_deltas 列表，它代表从起始日期开始到某个特定时间点经过的天数。
dates = [start_date + timedelta(days=td) for td in time_deltas]
# 将 datetime 对象转换为字符串，以便于阅读
date_strings = [str(date) for date in dates]
# 打印转换后的日期时间信息
for date_str in date_strings:
    print(date_str[0:11])
##日期处理结束，现在处理降水
date_range = pd.date_range('2003-01-01','2003-12-31')
df = pd.DataFrame(0,columns=['p'],index=date_range)
# dt = np.arrange(0,data.variables['time'].size)
dt = np.arange(0, len(time_data))

for time_index in dt:
    # 假设prec变量是一个三维数组，且时间、纬度和经度的维度分别是time, lat, lon
    # 你需要确保min_lat和min_lon是正确的索引值
    df.iloc[time_index] = prec[time_index, min_lat, min_lon]
# for time_index in dt:
#     df.iloc[time_index] = prec[time_index,min_lat,min_lat]

df.to_csv("jiangshui")