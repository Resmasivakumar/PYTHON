def amstrong(x):
    m=0
    l=str(x)
    n=len(l)
    while(x>0):
        a=x%10
        s=a**n
        m+=s
        x=x//10
        print(f"{s}")
    print(m)
           
amstrong(9474)