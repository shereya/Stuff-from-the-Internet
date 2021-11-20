#maximum frequency stack
l1=eval(input('Command array:'))
l2=eval(input('Array'))
n=len(l1)
l=['null']
l3=[]
for i in range(1,n):
    if l1[i]=="push" and l2[i]!=[]:
        l3=l3+l2[i]
        l.append('null')
    if l1[i]=="pop" and l2[i]==[]:
        c_max=0
        a=0
        L=[]
        for j in l3:
            if l3.count(j)>=c_max:
                c_max=l3.count(j)
                L.append(j)
        if len(L)>1:
            a=L[-1]
        l3=l3[::-1]
        for j in l3:
            if j==a:
                l3.remove(j)
                break
        l3=l3[::-1]
        l.append(a)
print(l)

        
        
                
            
