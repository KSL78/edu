a1 ,a2= ad = map(int, input().split())
ad = 0
if a1>=1 & a2<=1000:
    for i in range(a1,a2):
        ad=ad+i
    ad=ad-a1
    print(ad)
