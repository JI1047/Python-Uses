# 데이터 분석을 위한 pandas 라이브러리를 불러옵니다.
# 수치계산을 위한 numpy를 불러옵니다.
# 데이터 시각화를 위한 matplotlib, seaborn 을 불러옵니다.


# 히스토그램(histogram)은 표로 되어 있는 도수 분포를 정보 그림으로 나타낸 것
# 도수 분포(度數分布, frequency distribution) 또는 빈도분포는 표본의 다양한 산출 분포를 보여주는 목록, 표, 그래프
# 표에 들어가는 각 항목은 특정 그룹이나 주기 안에 값이 발생한 빈도나 횟수를 포함하고 있으며 이러한 방식으로 표는 표본 값의 분포를 요약

import pandas as pd #파일 포맷을 불러오는 역할을 한다.
import seaborn as sns
import matplotlib.pyplot as plt

#pandas 를 통해 다양한 형태의 데이터를 불러올 수 있다.

# sns.load_dataset("mpg")#자동차 연비 데이터 셋

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")

# df.hist(figsize=(10,8),bins=100)#hist를 통해서 히스토그램을 그린다.
# #figsize를 통해서 사이즈를 지정할 수 있다., bins는 막대의 개수이다.
# #막대가 붙어 있다면 연속된 데이터라는 것을 알 수 있다.
# plt.show()#화면 출력

#displot 을 통해 힉스토그램과 kedplot 그리기
# sns.displot(data=df, x="mpg",kde=True, rug=True)#kedplot을 통해서 밀도를 알 수 있다.

#kdeplot, ruglpt으로 밀도함수 그리기

# sns.kdeplot(data=df, x="mpg", shade=True, cut=2)#kedplot을 통해서 밀도를 알 수 있다.
# #shade=True: KDE 아래에 음영을 추가하여 KDE 아래 영역의 면적을 강조합니다.
# #cut=2: KDE를 그릴 때 끝을 어떻게 자를지를 결정합니다. 값이 크면 부드럽고 더 많은 데이터를 사용하며, 값이 작으면 뾰족한 부분에 더 집중됩니다

# sns.rugplot(data=df, x="mpg")#kedplot을 통해서 밀도를 알 수 있다.

# plt.show()

#agg 메서드를 사용하여 특정 열에 대한 여러 통계량을 한 번에 계산할 수 있습니다.
# print(df["mpg"].agg(["skew","kurt"]))

#  boxplot 을 통해서 데이터의 중앙값, 사분위수, 이상치 등을 시각적으로 보여주어 데이터의 분포를 파악
# sns.boxplot(data=df,  x="mpg")

#  violinplot상자 그림(box plot)과 커널 밀도 추정(kernel density estimation)을 결합한 그래픽으로, 데이터의 분포를 더 상세하게 시각화
# sns.violinplot(data=df,  x="mpg")

sns.violinplot(data=df)

plt.show()
