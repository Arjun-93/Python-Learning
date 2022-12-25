# Here I make the basic calculator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while(True):
    operator = input("Enter the operator: ")
    if(operator == "+"):
        print("The sum is: ", a + b)
        break
    if(operator == "-"):
        print("The difference is: ", a - b)
        break
    if(operator == "*"):
        print("The product is: ", a * b)
        break
    if(operator == "/"):
        print("The quotient is: ", a / b)
        break
    else:
        print("Invalid Operator")
    
