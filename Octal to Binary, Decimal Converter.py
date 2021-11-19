#octal to binary, hexadecimal, decimal
def OctaltoBinary(n):
    st_whole=''
    st_decimal=''
    s=''
    c=0
    l=[1,2,4]
    for i in str(n):
        if i!='.':
            st_whole=st_whole+i
            c=c+1
        else:
            break
    for i in str(n)[c+1::]:
        st_decimal=st_decimal+i
    for i in st_whole:
        if int(i) not in l and int(i)!=0:
            s1=0
            a=''
            if int(i)==l[0]+l[2]:
                s=s+'101'
            elif int(i)==l[1]+l[2]:
                s=s+'110'
            else:
                for j in l:
                    s1=s1+j
                    a=a+'1'
                    if s1==int(i) and len(a)<3:
                        a=a+'0'
                        break
                s=s+a[::-1]
        if int(i) in l and int(i)!=0:
            a=''
            for j in l:
                if int(i)==j:
                    a=a+'1'
                else:
                    a=a+'0'
            s=s+a[::-1]
        if int(i)==0:
            s=s+'000'
    s=s+'.'
    for i in st_decimal:
        if int(i) not in l and int(i)!=0:
            s1=0
            a=''
            if int(i)==l[0]+l[2]:
                s=s+'101'
            elif int(i)==l[1]+l[2]:
                s=s+'110'
            else:
                for j in l:
                    s1=s1+j
                    a=a+'1'
                    if s1==int(i) and len(a)<3:
                        a=a+'0'
                        break
                s=s+a[::-1]
        if int(i) in l and int(i)!=0:
            a=''
            for j in l:
                if int(i)==j:
                    a=a+'1'
                else:
                    a=a+'0'
            s=s+a[::-1]
        if int(i)==0:
            s=s+'000'
    s=s.lstrip('0')
    s=s.rstrip('0')
    if s[-1]=='.':
        s=s[0:len(s)-1]
    return s
def OctaltoDecimal(n):
    l_whole=[]
    l_decimal=[]
    s=0
    c=0
    for i in str(n):
        if i!='.':
            l_whole.append(int(i))
            c=c+1
        else:
            break
    l_whole=l_whole[::-1]
    for i in str(n)[c+1::]:
        l_decimal.append(int(i))
    for i in range(0,len(l_whole)):
        s=s+(l_whole[i]*(8**i))
    for i in range(1,len(l_decimal)+1):
        s=s+(l_decimal[i-1]*(8**-i))
    st=str(s).rstrip('0')
    if st[-1]=='.':
        st=st[0:len(st)-1]
    return st
    
num=float(input('Octal:'))
print(OctaltoBinary(num))
print(OctaltoDecimal(num))
            


    
    
            
                
            
        
                
            
