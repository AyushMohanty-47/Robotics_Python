a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))

p=a
q=b

while b!=0:
    a,b=b,a % b 

gcd=a
lcm=(p*q)/gcd

print("GCD: ", gcd)
print("LCM: ", lcm)