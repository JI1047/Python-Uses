import pandas as pd #파일 포맷을 불러오는 역할을 한다.
import seaborn as sns

#pandas 를 통해 다양한 형태의 데이터를 불러올 수 있다.

# sns.load_dataset("mpg")#자동차 연비 데이터 셋

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")
#pandas를 통해 불러오기


# print(df.head(3))#앞에서 부터 지정된 수만큼 데이터를 가져오게 할 수 있다.

# print(df.tail(3))#앞에서 부터 지정된 수만큼 데이터를 가져오게 할 수 있다.

# print(df.sample(3,random_state=42))#랜덤하게 데이터를 가져오게 된다.

#random_state를 통해 고정된 랜덤 데이터를 불러 올 수 있다.

# print(df.info())#info 를 통해 요약된 정보를 볼 수 있다.

#결측치 수 확인

# print(df.isnull().sum())#True 일 때 결측치라는 의미,수 확인
# print(df.isnull().mean() * 100) # 결측치를 비율로(백분율) 확인

#기술 통계 값

# print(df.describe())#기술 통계 값을 확인 할 수 있다.

# print(df["name"])#name 이라는 컬럼을 불러 올 수 있다.



#색인하기

#여러개의 컬럼을 가져오고 싶다면 list 형태로 묶어야 한다.

# print(df[["name","origin"]])#name 이라는 컬럼을 불러 올 수 있다.


# print(df["name"])#name 이라는 컬럼을 불러 올 수 있다.,1차원 형태


# print(df[["name"]])#name 이라는 컬럼을 불러 올 수 있다.2차원 형태


#행 인덱싱

#loc == locate loc로 하나의 행을 가져올 수 있다.

# print(df.loc[[0,1]])#2개 이상의 행은 리스트로 묶어서 데이터프레임 형태로 출력해주어야함

# print(df.loc[0,"name"])#행과 열을 가져오는 경우

print(df.loc[[0,1],["name","origin"]])#행과 열을 가져오는 경우



