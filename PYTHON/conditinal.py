x=int(input("Enter the Student mark:"))
if x<=500 and x>=400:
    print("Grade A")
elif x<=399:
    print("Grade B")
elif x<=299:
    print("Grade C")
elif x<=0:
    print("Grade d")
else:
    print("Fail")
print(x)