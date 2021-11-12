#print anagrams
l=eval(input('Array:'))
L1=[]
L2=[]
for i in range(0,len(l)):
    L=[l[i]]
    l1=[]
    for j in l[i]:
        l1.append(j)
    for j in range(i+1,len(l)):
        c=0
        for k in l[j]:
            if k in l1:
                c=c+1
        if len(l1)==c:
            L.append(l[j])
    if i==0:
        L1.append(L)
    else:
        C=0
        for k in L:
            for j in range(0,len(L1)):
                if k in L1[j]:
                    C=C+1
        if C==0:
            L1.append(L)
print(L1)
            

