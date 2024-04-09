import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df=sns.load_dataset("mpg")

# 비수치형 데이터인 경우에 해당 열은 "object"로 분류
# print(df.describe(include="object"))

# print(df.nunique())
# 수치가 높으면 Ex)연령,금액 수치형 데이터(일반적으로)
# 수치가 낮으면 EX)성별 범주형 데이터(일반적으로)

# countlplt 으로 origin 빈도수 시각화 하기
# sns.countplot(data=df, x="origin")

# origin 에 대해 빈도수
# print(df["origin"].value_counts())

# 2개 이상의 변수에 대한 시각화

# origin 빈도수를 시각화 하고 cylinders 로 다른 색상 표현하기
# sns.countplot(data=df, x="origin", hue="cylinders")

# cylinders의 빈도수를 시각화 하고 origin으로 다른 색상 표현하기
# sns.countplot(data=df, x="cylinders", hue="origin")

print(pd.crosstab(df["origin"],df["cylinders"]))


plt.show()