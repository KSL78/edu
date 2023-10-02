an=int(input())
a = []
for i in str(an):
    a.append(i)
a=sorted(a)
ang=a.reverse()
for i in a:
    print(i,end='')