#longest palindromic substring
#128/141 test cases passed
s=str(input('String:'))
palstr=s[0]
maxlen=1
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[i:j+1]==s[i:j+1][::-1] and len(s[i:j+1])>maxlen:
            palstr=s[i:j+1]
            maxlen=len(s[i:j+1])
print(palstr)
