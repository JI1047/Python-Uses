import requests
from bs4 import BeautifulSoup
import pymysql
db = pymysql.connect(
    host='localhost', # 127.0.0.1 , 0.0.0.0 
    port=3306, 
    user='root', # root
    passwd='Rlawltjr123@', 
    db='ecommerce', 
    charset='utf8')
cursor = db.cursor()

for page_num in range(10):#10페이지 까지의 범위
    if page_num == 0:#페이지가 0일때는 
        res = requests.get('https://davelee-fun.github.io/')#해당 페이지에 대한 get 요청보냄
    else:#페이지가 0이 아닐 때
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')#응답받은 페이지를 BeautifulSoup객체로 보냄
    data = soup.select('div.card-body')#제품정보 요소 선택
    for item in data:
        category = item.select_one('h2.card-title').get_text().replace('관련 상품 추천', '').strip()
        product = item.select_one('h4.card-text').get_text().replace('상품명:', '').strip()
        print (category, product)
        SQL = """INSERT INTO teddyproducts (TITLE, CATEGORY) VALUES('""" + product + """', '""" + category + """');"""
        print(SQL)
        cursor.execute(SQL)        

db.commit()
db.close()  
