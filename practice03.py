#since in practice02 almost exact code is repeated using while loop --> 
                       # create funcn. for code reusability
def get_number(nums):
    while True:
        num = input("\nEnter number" + str(nums) +": ")
        try:
            return float(num)
        except:
            print("\ninavlid number....try again")



num1 = get_number(1)
num2 = get_number(2)

sign = input("\nenter operation: ")
result = 0

if sign == "+":
    result = num1+num2

elif sign == "-":
    result = num1-num2

elif sign == "*":
    result = num1*num2

elif sign == "/":
    if num2 != 0:
        result = num1/num2
    else:
        print("\nDivision by 0 not possible")

elif sign == "%":
    result = num1%num2

elif sign == "**":
    result = num1**num2

else:
    print("\nInvalid sign...no operation.")

print("\nCalculator result is: ", result)