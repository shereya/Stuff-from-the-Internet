#company logo
s=str(input('Company Name:'))
l=[]
for i in s:
    l.append(i)
L=[]
L1=[]
for i in l:
    if l.count(i) not in L:
        L.append(l.count(i))
L.sort(reverse=True)
L=L[0:3]
L.sort(reverse=True)
for i in l:
    if i not in L1:
        L1.append(i)
L2=[]
L3=[]
for i in L1:
    if l.count(i) in L and l.count(i)!=min(L):
        L2.append(i)
    if l.count(i) in L and l.count(i)==min(L):
        L3.append(i)
L2.sort()
L3.sort()
f=True
while f==True:
    L2.append(L3[0])
    L3.remove(L3[0])
    if len(L2)>=3:
        f=False
L2=L2[0:3]
L2.sort()
for i in range(1,len(L2)):
    if l.count(L2[i])>l.count(L2[i-1]):
        L2[i],L2[i-1]=L2[i-1],L2[i]
for i in L2:
    print(i+' '+str(l.count(i)))




