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
    dv1 = (soup.find_all('table',class_="infobox"))
    dv2 = (soup.find_all('th',class_="infobox-label"))
    dv3 = (soup.find_all('td',class_="infobox-data"))
    # #print(soup)
    print(len(dv1))
    print(len(dv2))
    print(len(dv3))
    #print(dv2)
    for dv1f in dv1:
        dv1e = dv1f.find_all('th',class_="infobox-label")
        dv1a = dv1f.find_all('td',class_="infobox-data")
        for dv1r in dv1e:
            print(dv1r)
            
        for dv1t in dv1a:
            print(dv1t)
            print("/////////////////////////////")
    