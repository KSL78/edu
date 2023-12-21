
a = int(input())
al = []
re = []
def bfs(x,y):
    global cnv
    al[x][y] = 0
    
for i in range(a):
    al1 = input()
    al.append(al1)
print(al)
print(len(al))
for i in range(a):
    for x in range(a):
        print(al[i][x:x+1])
        if al[i][x:x+1]=="1":
            
            al[i][x:x+1]=0
        
print(al)
print(aw)