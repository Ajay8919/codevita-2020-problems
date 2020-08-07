
global forest
global l
global l1
forest=[['w','T','T','T','T','T'],
        ['T','w','w','w','w','T'],
        ['T','T','T','T','T','T'],
        ['w','w','w','w','w','T'],
        ['T','T','T','T','T','T'],
        ['T','T','w','w','w','w']]


l=[]


def check(x,y,m,n):
    if x<0 or y<0 or x>m-1 or y>n-1 :
        return False
    return True

def changeL1(x,y,m,n):
    if check(x+1,y,m,n) :
        if forest[x+1][y]=='T' :
            l1.append([x+1,y])
    if check(x,y+1,m,n) :
        if forest[x][y+1]=='T' :
            
            l1.append([x,y+1])
    if check(x-1,y,m,n) :
        if forest[x-1][y]=='T' :
            
            l1.append([x-1,y])
    if check(x,y-1,m,n) :
        if forest[x][y-1]=='T' :
            
            l1.append([x,y-1])
    if check(x+1,y+1,m,n) :
        if forest[x+1][y+1]=='T' :
            
            l1.append([x+1,y+1])
    if check(x-1,y-1,m,n) :
        if forest[x-1][y-1]=='T' :
            
            l1.append([x-1,y-1])
    if check(x+1,y-1,m,n) :
        if forest[x+1][y-1]=='T' :
            
            l1.append([x+1,y-1])
    if check(x-1,y+1,m,n) :
        if forest[x-1][y+1]=='T' :
            
            l1.append([x-1,y+1])

def changeL(x,y,m,n):
    if check(x+1,y,m,n) :
        if forest[x+1][y]=='T' and [x+1,y] not in l1:
            l.append([x+1,y])
    if check(x,y+1,m,n) :
        if forest[x][y+1]=='T' and [x,y+1] not in l1:
            
            l.append([x,y+1])
    if check(x-1,y,m,n) :
        if forest[x-1][y]=='T' and [x-1,y] not in l1:
            
            l.append([x-1,y])
    if check(x,y-1,m,n) :
        if forest[x][y-1]=='T' and [x,y-1] not in l1:
            
            l.append([x,y-1])
    if check(x+1,y+1,m,n) :
        if forest[x+1][y+1]=='T' and [x+1,y+1] not in l1:
            
            l.append([x+1,y+1])
    if check(x-1,y-1,m,n) :
        if forest[x-1][y-1]=='T' and [x-1,y-1] not in l1:
            
            l.append([x-1,y-1])
    if check(x+1,y-1,m,n) :
        if forest[x+1][y-1]=='T' and [x+1,y-1] not in l1:
            
            l.append([x+1,y-1])
    if check(x-1,y+1,m,n) :
        if forest[x-1][y+1]=='T' and [x-1,y+1] not in l1:
            
            l.append([x-1,y+1])



x=0 #xy are start fire cordinates
y=5 
m=6 #row length
n=6 #column length
l1=[]
l=[]
c=1
forest[x][y]=1
changeL1(x,y,m,n)

while(len(l1)!=0) :
    l=[]
    while(len(l1)!=0):
        #print(l1)
        co=l1.pop()
        a,b=co[0],co[1]
        forest[a][b]=c
        changeL(a,b,m,n)
    l1=l
    c+=1


print(c)

        
    
    
