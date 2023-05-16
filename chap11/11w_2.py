#========ppt 웹 기반 빅데이터 수집실습===========

#pip install selenium
#pip install webdriver_manager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)

#
#=========네이버 뉴스 크롤링========
driver.get("https://naver.com")
time.sleep(5)  #몇초동안 띄어 놓을 건지 설정함

#뉴스버튼 우클릭-> 검사 ->tag 우클릭->copy-> copy full xpath ->/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a
#element를 찾은 다음에 뉴스 버튼을 클릭해라
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a').click()
time.sleep(3)
newstitle =driver.find_element(By.XPATH,'/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/a/div[2]/h4').text
print(newstitle)

#============= 부동산 거래 내역 및 관련 내용 수집하기 ==============
driver.get("https://m.land.naver.com/search")
time.sleep(3)
#입력창 크롤링-> 입력창 클릭
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input').click()
time.sleep(3)
#입력창에 부동산 입력
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input').send_keys("여의도동 여의도파라곤")
time.sleep(1)
#입력창 옆에 버튼 클릭
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i').click()
time.sleep(3)
#전세,매매 크롤링
salePrices = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd').text
jeonse = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd').text
print(salePrices)
print(jeonse)

#================ 주식 관련 정보 수집하기 =================
'''if __name__ =="__main__":
    driver.get("https://finance.daum.net/quotes/A005380#home")
    time.sleep(3)
    price1= driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/span').text
    price2= driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[8]/span').text
    price3= driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr[3]/td[8]/span').text
    price4= driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr[4]/td[8]/span').text
    price5= driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/table/tbody/tr[5]/td[8]/span').text

    print(price1)
    print(price2)
    print(price3)
    print(price4)
    print(price5)'''

driver.get('https://finance.naver.com/')
time.sleep(3)
lst=[]
for i in range(10):
    subject=driver.find_element(By.XPATH,f'/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]').text
    lst.append(subject)
print(lst)