import cftime
import pandas as pd
from netCDF4 import Dataset, num2date
import numpy as np
import os
import siteinfo

# 设置包含nc文件的文件夹路径
sname = 'CBS'
folder_path = r'C:\Users\Administrator\Desktop\fluxdata\CMFD\temp'

# 获取文件夹中所有的nc文件
nc_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.nc')]
print("Files found:", len(nc_files))

# 遍历所有的nc文件
for file in nc_files:
    data = Dataset(file)
    print(f'Opened file: {file}')

    # 提取经纬度数据和温度
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]

    lat_T = siteinfo.stations_coordinates[sname]['lat']
    lon_T = siteinfo.stations_coordinates[sname]['lon']

    sq_lat = (lat - lat_T) ** 2
    sq_lon = (lon - lon_T) ** 2
    min_lat_idx = sq_lat.argmin()
    min_lon_idx = sq_lon.argmin()

    temp = data.variables['temp'][:]
    time_var = data.variables['time']
    time_data = num2date(time_var[:], units=time_var.units, calendar=time_var.calendar if 'calendar' in dir(time_var) else 'standard')

    # Convert cftime to datetime
    standard_time = [pd.Timestamp(str(date)) for date in time_data]

    # 创建DataFrame
    df = pd.DataFrame({'Temperature': temp[:, min_lat_idx, min_lon_idx]}, index=pd.DatetimeIndex(standard_time))

    # 按日重新采样并计算平均温度、最高温度和最低温度
    daily_df = df.resample('D').agg({'Temperature': ['mean', 'max', 'min']})
    daily_df.columns = ['Average_Temperature', 'Max_Temperature', 'Min_Temperature']

    # 保存为CSV
    output_filename = f'{sname}Temp_Daily_{os.path.basename(file).replace(".nc", ".csv")}'
    output_file = os.path.join(folder_path, output_filename)
    daily_df.to_csv(output_file)
    print(f'{sname}Temperature data has been saved to file: {output_file}')

    data.close()
