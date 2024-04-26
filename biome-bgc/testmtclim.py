import mtclim
import pandas as pd
# 假设您已经将CSV数据加载到DataFrame中
df = pd.read_csv(r'C:\Users\Administrator\Desktop\fluxdata\finishtemp\CBScombined_csv.csv')

# 使用mtclim进行处理
results = mtclim.run_mtclim(df)

# 打印或保存结果
print(results)