print("WELCOME TO CALCULATOR")

a=int(input("Enter first Number: "))
b=int(input("Enter second Number: "))

print("Choose Operations to perform: ")
print("Press 1 for Addition")
print("Press 2 for Subbtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

operation=int(input("enter your operator: "))

if(operation==1):
    print("Sum is: ",a+b)

elif(operation==2):
    print("Difference is: ",a+b)

elif(operation==3):
    print("Product is: ",a*b)

elif(operation==4):
    if(b!=0):
        print("Quotient is: ",a/b)
    else:
        print("Not Defined")

else:
    print("Choose between 1 to 4 ONLY")