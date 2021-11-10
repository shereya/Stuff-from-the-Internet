
words=eval(input('words='))
puzzles=eval(input('puzzles='))
l=[]
for i in puzzles:
    b=0
    for j in words:
        c=0
        for k in j:
            if k in i:
                c=c+1
        if c==len(j) and i[0]==j[0]:
            b=b+1
    l.append(b)
print(l)
