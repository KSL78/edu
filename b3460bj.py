a1 = int(input())
for _ in range(a1):
    a = int(input())
    va2=[]
    
    while True:
        vl1=a//2
        vl2=a%2
        va2.append(vl2)
        if vl1<2:
            va2.append(vl1)
        a=a//2
    
        if a<2:
            break
        
    for v1 in range(len(va2)):
        if va2[v1]==1:
            print(v1, end=' ')

