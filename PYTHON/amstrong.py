def reverse(x):
    m=len(x)
    while(x>0):
        a=x%10
        m=(m*10)+a
        x=x//10
    print(m)
reverse(153)