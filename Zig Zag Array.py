l=eval(input('List:'))
if len(l)%2==1:
    for i in range(1,len(l),2):
        if l[i-1]<l[i]>l[i+1]:
            continue
        else:
            if l[i-1]>l[i]:
                l[i-1],l[i]=l[i],l[i-1]
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
if len(l)%2==0:
    a=l.pop()
    for i in range(1,len(l),2):
        if l[i-1]<l[i]>l[i+1]:
            continue
        else:
            if l[i-1]>l[i]:
                l[i-1],l[i]=l[i],l[i-1]
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    l.append(a)
    if l[-2]>l[-1]:
        l[-1],l[-2]=l[-2],l[-1]
print(l)
