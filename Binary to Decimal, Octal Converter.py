#from binary to decimal, octal, hexadecimal converter
def BinarytoDecimal(n):
    l_whole=[]
    l_decimal=[]
    l=[]
    c=0
    c_whole=0
    c_decimal=0
    for i in str(n):
        l.append(i)
    for i in l:
        if i!='.':
            c=c+1
        else:
            break
    for i in l[0:c]:
        l_whole.append(int(i))
    for i in l[c+1::]:
        l_decimal.append(int(i))
    l_whole=l_whole[::-1]
    for i in range(0,len(l_whole)):
        c_whole=c_whole+(l_whole[i]*(2**i))
    for i in range(1,len(l_decimal)+1):
        c_decimal=c_decimal+(l_decimal[i-1]*(2**(-i)))
    return c_whole+c_decimal
def BinarytoOctal(n):
    l_whole=[]
    l_decimal=[]
    l=[]
    c=0
    L_whole=[]
    L_decimal=[]
    l1=[]
    l2=[]
    for i in str(n):
        l.append(i)
    for i in l:
        if i!='.':
            c=c+1
        else:
            break
    for i in l[0:c]:
        l_whole.append(int(i))
    for i in l[c+1::]:
        l_decimal.append(int(i))
    l_whole=l_whole[::-1]
    if len(l_whole)%3!=0:
        f=False
        while f==False:
            l_whole.append(0)
            if len(l_whole)%3==0:
                f=True
    for i in l_whole:
        l1.append(i)
        if len(l1)==3:
            L_whole.append(l1[::-1])
            l1=[]
    if len(l_decimal)!=0:
        if len(l_decimal)%3!=0:
            f=False
            while f==False:
                l_decimal.append(0)
                if len(l_decimal)%3==0:
                    f=True
    for i in l_decimal:
        l2.append(i)
        if len(l2)==3:
            L_decimal.append(l2)
            l2=[]
    st=''
    octal=[4,2,1]
    L_whole=L_whole[::-1]
    for i in L_whole:
        s=0
        for j in range(3):
            s=s+(i[j]*octal[j])
        st=st+str(s)
    if len(l_decimal)!=0:
        st=st+'.'
    for i in L_decimal:
        s=0
        for j in range(3):
            s=s+(i[j]*octal[j])
        st=st+str(s)
    return st, l_decimal


        
            
            
            










        
num=float(input('Binary:'))
print(BinarytoOctal(num))
