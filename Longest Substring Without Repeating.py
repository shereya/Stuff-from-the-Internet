#longest substring without repeating
s=str(input('String:'))
l=[]
L=[]
L1=[]
for i in s:
    l.append(i)
for i in range(0,len(l)):
    for j in range(1,len(l)):
        a=l[i:j]
        if a!=[]:
            L.append(a)
            
for i in L:
    c=0
    for j in i:
        if i.count(j)==1:
            c=c+1
    if c==len(i):
        L1.append(i)
lenmax=0
for i in L1:
    if len(i)>lenmax:
        lenmax=len(i)
print(lenmax)
    
