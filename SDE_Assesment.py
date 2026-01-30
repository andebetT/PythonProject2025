def getMaxSolar(s):
    s=list(s)
    count=0
    n=len(s)
    for i in range(len(s)):
        if s[i]=="1":
            count+=1
    for i in range(len(s)):
        if s[i]=="0":
            istrue=True
            if i>0 and s[i-1]=="1":
                istrue=False
            if i<n-1 and s[i+1]=="1":
                istrue=False

            if istrue:
                count+=1
                s[i]="1"
    print(s)
    return count

s="1111110001"
print(getMaxSolar(s))



for i in range(4):
    print("hi",end="&")
