
def chessBoard(q,chess,visited,adjacent,n):
    visited.add(q[2])
    cur_x=q[0]
    cur_y=q[1]
    name=q[2]
    Max=1
    if(len(adjacent[name])==0):
        visited.remove(name)
        return Max
    
    for i in adjacent[name]:
        if i[2] not in visited:
            path=chessBoard(i,chess,visited,adjacent,n)
            Max=max(1+path,Max)
    visited.remove(name)
    return Max
    
    
    

def adjacency(chess,i,j,n,adjacent,q):
    for y in range(j+1,n):
        if(chess[i][y]!=0):
            adjacent[q].append((i,y,chess[i][y]))
            break
    for x in range(i+1,n):
        if(chess[x][j]!=0):
            adjacent[q].append((x,j,chess[x][j]))
            break
    for y in range(j-1,-1,-1):
        if(chess[i][y]!=0):
            adjacent[q].append((i,y,chess[i][y]))
            break
    for x in range(i-1,-1,-1):
        if(chess[x][j]!=0):
            adjacent[q].append((x,j,chess[x][j]))
            break
    #right top corner
    x,y=i-1,j+1
    while(x>-1 and y<n):
        if(chess[x][y]!=0):
            adjacent[q].append((x,y,chess[x][y]))
            break
        x-=1
        y+=1
    #left top corner
    x=i-1
    y=j-1
    while(x>-1 and y>-1):
        if(chess[x][y]!=0):
            adjacent[q].append((x,y,chess[x][y]))
            break
        x-=1
        y-=1
    #right down corner
    x=i+1
    y=j+1
    while(x<n and y< n):
        if(chess[x][y]!=0):
            adjacent[q].append((x,y,chess[x][y]))
            break
        x+=1
        y+=1
    #left down corner
    x=i+1
    y=j-1
    while(x<n and y>-1):
        if(chess[x][y]!=0):
            adjacent[q].append((x,y,chess[x][y]))
            break
        x+=1
        y-=1
            
c,n=map(int,input().split())
queens=[]
chess=[[0 for i in range(c)]for j in range(c)]
for i in range(n):
    x,y,q=input().split()
    x=int(x)
    y=int(y)
    chess[x-1][y-1]=q
    queens.append((x-1,y-1,q))


adjacent={}
#print(c,n,queens)
Max=0
for q in queens:
    adjacent[q[2]]=[]
    adjacency(chess,q[0],q[1],c,adjacent,q[2])

for i in queens:
    start=i[2]
    visisted=set()
    Max=max(Max,chessBoard(i,chess,visisted,adjacent,c))

print(n-Max+1)





