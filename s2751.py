import sys
input=sys.stdin.readline
a=int(input())
ad = []
for i in range(a):
    ad.append(int(input())) 
for i in sorted(ad):
    print(i)
    
