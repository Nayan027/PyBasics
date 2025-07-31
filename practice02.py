while True:
    num1 = input("Enter a number: ")
    try:
        num1 = float(num1)
        break
    except:
        print("invalid number, try again")

while True:
    num2 = input("Enter 2nd number: ")
    try:
        num2 = float(num2)
        break
    except:
        print("invalid number, try again")


result = 0
operation = input("\nassign operation: ")
print("Generic expression of ur calcualtion: ",num1, operation, num2)

if operation == "+":
    result = num1 + num2

elif operation == "*":
    result = num1*num2

elif operation == "-":
    result = num1-num2

elif operation == "/":
    result = num1/num2

elif operation == "%":
    result = num1%num2

elif operation == "**":
    result = num1**num2

else:
    print("\nInvalid operation asked to perform.")


print("\nResult of the calculator is:",result)