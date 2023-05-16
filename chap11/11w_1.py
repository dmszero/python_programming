#=======ppt  웹기반 빅데이터 수집 실습

#pip install beautifulsoup4 -->bs4 오류 발생 시 인터프리터 변경 ctrl+shift+p =>select interprinter ->pythoon base 선택
from bs4 import BeautifulSoup

#http 요청 처리 library
import requests 

headers ={
    "User-Agent":"dmszero"
} 
#news crolling 
webpage=requests.get("https://n.news.naver.com/mnews/article/029/0002800711",headers=headers)
print(webpage)
#news html
soup = BeautifulSoup(webpage.content,"html.parser")
print(soup)
#news text
news=soup.select_one("#dic_area").getText().strip()
print(news)



