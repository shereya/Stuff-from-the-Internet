#password validation
def CheckPassword(s):
    l=[]
    for i in s:
        l.append(i)
    count_caps=0
    count_digit=0
    count_slashspace=0
    if len(l)>=4 and str(l[0]) not in '0123456789':
        for i in l:
            if i.isdigit()==True:
                count_digit=count_digit+1
            if ord(i)>=65 and ord(i)<=90:
                count_caps=count_caps+1
            if i=='''/''':
                count_slashspace=count_slashspace+1
            if i==' ':
                count_slashspace=count_slashspace+1
        if count_caps>=1 and count_digit>=1 and count_slashspace==0:
                return 1
        else:
            return 0
    else:
        return 0
pwd=str(input('Password:'))
print(CheckPassword(pwd))
