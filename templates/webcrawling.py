from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

url = 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
html = req.get(url) #웹사이트 가져오기
#pprint(html.text)
soup = bs(html.text,'html.parser')  #beatuifulsoup로 재DOM\화

finedust = soup.find('div', {'class' : 'detail_box'})   #미세먼지 영역 찾기
#pprint(finedust)
details = finedust.findAll('dd')    #요소 3개 찾기
#print(details)

#미세먼지
finedust = details[0].find('span', {'class', 'num'}).get_text()
pprint(finedust)

#초미세먼지
ultrafineduest = details[1].find('span', {'class', 'num'}).get_text()

#오존지수  
ozone = details[2].find('span', {'class', 'num'}).get_text()

print('{0}, {1}, {2}'.format(finedust, ultrafineduest, ozone))