def power(base_num,pow_num):
    result=1
    for x in range(pow_num):
        result = result * base_num
    return result 
num1=float(input("please inter the first number: "))
operator=input("please ente your operator { + , - , * , / , % , ^}: ")
num2=float(input("please inter the second number: "))
if operator == "+":
    print(num1," + ",num2, " = ",num1+num2)
elif operator == "-":
    print(num1," - ",num2, " = ",num1 - num2)
elif operator == "*":
    print(num1," * ",num2, " = ",num1 * num2)
elif operator == "/":
    print(num1," / ",num2, " = ",num1 / num2)
elif operator == "%":
    print(num1," % ",num2, " = ",num1 % num2)
elif operator =="^":
    num1=int(num1)
    num2=int(num2)
    p=power(num1,num2)
    print(num1," ^ ",num2, " = ",p) 
else:
    print("Wrong operator")