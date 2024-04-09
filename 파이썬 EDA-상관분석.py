import pandas as pd #파일 포맷을 불러오는 역할을 한다.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#pandas 를 통해 다양한 형태의 데이터를 불러올 수 있다.

sns.load_dataset("mpg")#자동차 연비 데이터 셋

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")



df_numeric = df.select_dtypes(include=['number']) # 숫자형 데이터만 있는 열 선택
corr=df_numeric.corr() # 상관 분석 수행

mask =np.triu(np.ones_like(corr))
print(mask)

sns.heatmap(corr, annot=True, cmap="coolwarm", vmax=1, vmin=-1,mask=mask)

plt.show()
