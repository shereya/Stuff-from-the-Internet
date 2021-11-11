#paranthesis checker
s=str(input('String:'))
s1=''
S=''
l=[]
for i in s:
    s1=s1+i
    if len(s1)%2==0 and len(s1)!=2:
        if ord(s1[len(s1)-1])==ord(s1[0])+2:
            l.append(s1)
            s1=''
    if len(s1)==2:
        if s1=='()' or s1=='[]' or s1=='{}':
            l.append(s1)
            s1=''
for i in l:
    S=S+i
if S==s:
    print('true')
else:
    print('false')
        
        
        
    
