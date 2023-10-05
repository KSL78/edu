s = int(input())
z = 0
k = 0
for i in range(1,s+1):
    z+=1
    k+=z
    if k>s:
        z-=1
        break
print(z)