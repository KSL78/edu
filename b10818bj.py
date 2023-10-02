a=int(input())
if a>0 & a<1000000:
    ad = list(map(int, input().split()))
    ad=sorted(ad)
    print(ad[0])
    print(ad[len(ad)-1])
