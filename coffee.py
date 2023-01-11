def mo(a,b):
    a = a + b
    return a

li = {"ame":1000,"latte":1500,"calamel":2000}
money = int(input("돈을 넣어주세요"))
while money>=1000:
    print("커피를 선택해 주세요\n아메리카노=a,라떼=l,카라멜=c")
    se = input()
    if se == "a":
        if money<li["ame"]:
            print("돈이 부족합니다 돈을 더 넣어주세요")
            moneyp = int(input())
            money =mo(money,moneyp)
        else :
            print("아메리카노커피가 나왔습니다.")
            money = money-li["ame"]
    elif se == "l":
        if money<li["latte"]:
            print("돈이 부족합니다 돈을 더 넣어주세요")
            moneyp = int(input())
            money =mo(money,moneyp)
        else :
            print("라떼커피가 나왔습니다.")
            money = money-li["latte"]
    elif se == "c":
        if money<li["calamel"]:
            print("돈이 부족합니다 돈을 더 넣어주세요")
            moneyp = int(input())
            money =mo(money,moneyp)
        else :
            print("카라멜커피가 나왔습니다.")
            money = money-li["calamel"]
if money<1000:  
    print("잔돈은 %d 입니다."%money)