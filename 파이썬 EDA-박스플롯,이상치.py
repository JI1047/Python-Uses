import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df=sns.load_dataset("mpg")


sns.boxenplot(data=df, x="origin",y="mpg")

origin_desc=df.groupby("origin")["mpg"].describe()

europe=origin_desc.loc["europe"]
Q3= europe["75%"]
Q1= europe["25%"]
IQR= Q3-Q1

OUT_MAX = Q3 + (1.5 * IQR)
OUT_MIN = Q1 - (1.5 * IQR)

# print(OUT_MAX,OUT_MIN)
plt.show()