a = int(input())
ad=[]
for i in range(1,a+1):
    x = input()
    ad.append(x)

ad=set(ad)

ad=sorted(ad)

ad.sort(key=len)
for i in ad:
    print(i)




