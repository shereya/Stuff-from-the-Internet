#autobiographical number
def AutobiographicalNum(n):
    s=str(n)
    l=[]
    c=0
    l1=[]
    for i in s:
        l.append(i)
    for i in range(0,len(l)):
        a=l.count(str(i))
        if str(a)==l[i]:
            c=c+1
    if c==len(l):
        print('Yes')
        for i in l:
            if i not in l1:
                l1.append(i)
        print(len(l1))
    else:
        print('No')
N=int(input('Number:'))
if len(str(N))>11:
    print('Error')
else:
    AutobiographicalNum(N)
