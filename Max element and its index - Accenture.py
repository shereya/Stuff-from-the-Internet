#maximum element and its index
l=eval(input('Array:'))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)

element_max=0
index=0
for i in range(0,len(l1)):
    if l1[i]>element_max:
        element_max=l[i]
        index=i
print(element_max)
print(index)
