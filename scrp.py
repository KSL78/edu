from requests import get

#사이트가 이러한 규칙으로 되어 있을 경우만 가능
#프로젝트 종료(실패)
'''base_url = ""#사이트 명 입력
search_tx = ""#사이트에서 검색 할 내용 입력'''
#위키 피디아 최적화
from bs4 import BeautifulSoup

burl = "https://ko.wikipedia.org/wiki/T-55"
#resp = get(f"{base_url}{search_tx}")
resp = get(f"{burl}")
if resp.status_code !=200:
    print('웹 사이트가 정보 제공을 거부합니다.')
else:
    #print(resp)
    soup = BeautifulSoup(resp.text,"html.parser")
    dv1 = (soup.find_all('table',class_="infobox"))
    # dv2 = (soup.find_all('th',class_="infobox-label"))
    # dv3 = (soup.find_all('td',class_="infobox-data"))
    # #print(soup)
    # print(len(dv1))
    # print(len(dv2))
    # print(len(dv3))
    #print(dv2)
    dv2c = []
    dv3c = []
    dvm = 0
    for dv1a in dv1:
        
        dv2a = dv1a.find_all('th',class_="infobox-label")
        dv3a = dv1a.find_all('td',class_="infobox-data")
        # print(len(dv2a))
        # print(len(dv3a))
        dv1n = len(dv2a)

        for dv2b in dv2a:
            dv2c.append(dv2b.string)
        for dv3b in dv3a:
            if len(dv3b)!=1:
                #print(dv3b)
                dv3sp = dv3b.find_all('a')
                #print(dv3sp[-1].string)
                dv3c.append(dv3sp[-1].string)
            else :
                dv3c.append(dv3b.string)
    while dv1n>dvm:
        print(str(dv2c[dvm])+":"+str(dv3c[dvm]))
        print("/////////////")
        dvm+=1
    print(dv1n)
    print(dvm)

        
            
        
    