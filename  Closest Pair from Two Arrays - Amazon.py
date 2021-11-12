#closest pair from two arrays
l1=eval(input('Array 1:'))
l2=eval(input('Array 2:'))
x=int(input('X:'))
l1.sort()
l2.sort()
l=[]
L=[]
for i in l1:
    for j in l2:
        l.append([i,j])
for i in l[0]:
    S=0
    if x>S:
        mindiff=x-S
    if x==S:
        mindiff=0
    else:
        mindiiff=S-x
for i in l:
    s=0
    for j in i:
        s=s+j
    if x>=s:
        d=x-s
        if d<mindiff:
            mindiff=d
    if s>x:
        d=s-x
        if d<mindiff:
            mindiff=d
for i in l:
    s1=0
    for j in i:
        s1=s1+j
    if x>=s1:
        d=x-s1
        if d==mindiff:
            L.append(i)
    if s1>x:
        d=s1-x
        if d==mindiff:
            L.append(i)
if len(L)>1:
    print(L[0])
else:
    for i in L:
        print(i)

