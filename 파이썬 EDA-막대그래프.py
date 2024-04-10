import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df=sns.load_dataset("mpg")

# # 범주/수치 형 변수를 막대그래프로 표현
# sns.barplot(data=df, x="origin", y="mpg", estimator=np.mean,ci=95, palette="muted")
# # estimator=np.mean로 각 범주에 대한 대푯값을 설정(막대 그래프의 높이를 나타냄)ci=95(신뢰 구간)

# group by

# # 그룹화하여 평균 계산
# print(df.groupby("origin").mean())

# pivot_table을 통한 연산
# print(pd.pivot_table(data=df, index="origin",values="mpg"))

# barplot 에 hue를 사용하여 색상을 다르게 표현해 보기
# sns.barplot(data=df, x="cylinders", y="mpg",ci=None, hue="origin")

# pivot_table을 통해 위 시각화 대한 값을 구하기

# print(pd.pivot_table(data=df, index="cylinders",columns="origin",values="mpg"))


# cylinders 와 mpg 의 x,hue 값을 변경해서 시각화

sns.barplot(data=df, x="origin", y="mpg",ci=None, hue="cylinders", palette="muted")
plt.show()
