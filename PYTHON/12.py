n=5
for i in range(1,n+1):
    s=" "
    for k in range(n-i):
        s+=" "
    for j in range(1,i+1):
        s+=str(j)
        s+=" "
        
    print(s)
        