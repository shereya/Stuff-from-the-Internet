#replace frequent character
def ReplaceFrequentCharacter(s,char):
    replaced_s=''
    l=[]
    l1=[]
    l2=[]
    freq_char=''
    c=0
    for i in s:
        l.append(i)
    for i in l:
        if l.count(i)>=c:
            c=l.count(i)
            freq_char=i
            l1.append(i)
    for i in l1:
        if i not in l2:
            l2.append(i)
    l3=[l2[0]]
    for i in l2:
        if ord(i)<ord(l2[0]):
            l3.remove(l2[0])
            l3.append(i)
    freq_char1=l3[0]
    for i in l:
        if i==freq_char1:
            replaced_s=replaced_s+char
        else:
            replaced_s=replaced_s+i
    print(replaced_s)            
st=str(input('String:'))
character=str(input('Character:'))
ReplaceFrequentCharacter(st,character)
