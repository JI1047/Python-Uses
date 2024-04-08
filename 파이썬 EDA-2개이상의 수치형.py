import pandas as pd #파일 포맷을 불러오는 역할을 한다.
import seaborn as sns
import matplotlib.pyplot as plt

#pandas 를 통해 다양한 형태의 데이터를 불러올 수 있다.

sns.load_dataset("mpg")#자동차 연비 데이터 셋

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")

#scatterplot을 통해서 x,y간의 산점도를 통해 시각화
# sns.scatterplot(data=df, x="weight", y="mpg", hue="origin")
#hue를 통해서 열의 값에 따라 색상을 설정 할 수 있다.

# 회귀 시각화
# 회귀선은 데이터의 경향을 파악하고 예측하는 데 사용됩니다. 
# 예를 들어, x,y사이의 관계를 분석할 때, 회귀선을 사용하여 x에 따라 y가 어떻게 변하는지 예측할 수 있습니다.

# sns.regplot(data=df, x="weight",y="mpg")
#regplot에서는 hue를 지원하지 않는다

# lmplot를 통해 범주값에 따라 색상, 서브플롯을 그릴 수 있다.
# sns.lmplot(data=df,  x="weight", y="mpg", hue="origin", col="origin", truncate=False)
# col을 이용하여 값들을 서브플롯(하나의 그래프 영역을 작은 영역으로 나누어 표현하는 법)생성
# truncate을 이용하여 회귀선을 그릴때 마다 포인터를 그대로 유지하거나 데이터를 잘라서 표시하게 할 수 있다.

#joinplot
# sns.jointplot(data=df,  x="weight", y="mpg", kind="reg")
#kind를 통해 그래프의 유형을 정할 수 있다.


# 잔차 시각화
# 회귀 분석을 통해 얻은 모델의 예측값과 실제 값 사이의 차이인 잔차를 시각적으로 분석
# sns.residplot(data=df, x="weight",y="mpg")


# df_sample=df.sample(100)

# #데이터프레임 내의 모든 변수들 간의 관계를 시각적으로 탐색 속도가 오래걸림
# sns.pairplot(df_sample, hue="origin")

#lineplot

# sns.lineplot(data=df, x="model_year", y="mpg", ci=None)

#relplot 으로 수치형 변수에 따라 서브플롯을 그린다.
# sns.relplot(data=df, x="model_year",  y="mpg", col="origin", hue="origin")

sns.relplot(data=df)

plt.show()