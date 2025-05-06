Tamil=int(input("Enter the Tamil mark:"))
English=int(input("Enter the English mark:"))
Maths=int(input("Enter the Maths mark:"))
Science=int(input("Enter the science mark:"))
social=int(input("Enter the Social mark:"))
Total=Tamil+English+Maths+Science+social
if Total>=0 and Total<=500:
    if Total<=500 and Total>=400:
        print("Grade A")
    elif Total<=399 and Total>=300:
        print("Grade B")
    elif Total<=299 and Total>=200:
        print("Grade C")
    elif Total>=0:
        print("Grade d")
    else:
         print("fail")
else:   
    print("The Number is invalid")
print(Total)
