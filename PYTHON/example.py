import random
def generate_otp(n):
    otp=""
    for i in range(n):
        s=random.randint(0,9)
        otp+=str(s)
    print(otp)
generate_otp(4)
    
