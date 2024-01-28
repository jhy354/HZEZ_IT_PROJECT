import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel("data.xlsx")
print(df)
df1 = df[(df.日期 == "01-13") & (df.时间 == "8时")] # 两边括号必须加, &比较的是bool型
print(df1)
df1 = df1.groupby("学号", as_index=False).次数.count()
df1 = df1.sort_values("次数", ascending=False)
plt.bar(df1.学号, df1.次数)
plt.xlabel("学号")
plt.ylabel("警告次数")
plt.show()