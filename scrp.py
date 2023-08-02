from requests import get
#사이트가 이러한 규칙으로 되어 있을 경우만 가능
'''base_url = ""#사이트 명 입력
search_tx = ""#사이트에서 검색 할 내용 입력'''
#위키 피디아 최적화
from bs4 import BeautifulSoup

burl = "https://ko.wikipedia.org/wiki/T-64"
#resp = get(f"{base_url}{search_tx}")
resp = get(f"{burl}")
if resp.status_code !=200:
    print('웹 사이트가 정보 제공을 거부합니다.')
else:
    #print(resp)
    soup = BeautifulSoup(resp.text,"html.parser")
    print(soup.find_all('div',class_="mw-parser-output"))
    #print(soup)
