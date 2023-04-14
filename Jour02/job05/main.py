def calculate(num1, operator, num2):
    if operator == "+":
        return num1+num2
    elif operator =="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    else: 
        print("opérateur non valide")


result = calculate(78,"+",3)
print(result)
result = calculate(36,"-",3)
print(result)
result = calculate(43,"*",2)
print(result)
result = calculate(36,"o",3)
print(result)