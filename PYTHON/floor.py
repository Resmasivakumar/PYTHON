# x=153
# n=1//10
# print(n)
def amstrong(x):
    len=3
    while(x>0):
        a=x%10
        s=a**len
        x+=s
        x=x//10
        print(s)
        break
amstrong(153)