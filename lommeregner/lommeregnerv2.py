

#variabler
num1 = float(input("skriv først tal: "))
num2 = float(input("skriv andet tal: "))

sign = input("skriv operator: ")
if sign == '+' or '-' or '*' or '/':

    if sign == '+':
        print("svaret er", num1 + num2)

    elif sign == '-':
        print("svaret er", num1 - num2)

    elif sign == '*':
        print("svaret er", num1 * num2)

    elif sign == '/':
        print("svaret er", num1 / num2)

else:
    print("fejl")
