#build a calculator with basic operations.
#take 2 inputs
#take operator as an input(+, -, *, /)
#check if + then print(a + b

a = input("enter first number")
b = input("enter second number")
c = input ("enter the opearation you want to perform")
if c == "+":
    print(int(a) + int(b))
elif c == "-":
    print(int(a) - int(b))
elif c == "*":
    print(int(a) * int(b))
elif c == "/":
    print(int(a) / int(b))
else:
    print("invalid operator")

