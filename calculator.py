
num1 = int(input("Please, enter the first number: "))
num2 = int(input("Please, enter the second number: "))
operation = input("Choose your operation[p:Plus, m:Minus, d:Devide, t:Multiply]: ")
if operation == "p":
    def plus(num1,num2):
        sum = num1 + num2
        print(num1, '+', num2, '=', sum)
    plus(num1,num2)

elif operation == "m":
    def minus(num1, num2):
        sum = num1 - num2
        print(num1, '-', num2,'=', sum)
    minus(num1, num2)

elif operation == "d":
    def division(num1, num2):
        if num2 == 0:
            print("You can not devide numbers by Zero")
        else:
            sum = num1/num2
            print(num1, ' / ', num2, ' = ', sum)

    division(num1, num2)

elif operation == "t":
    def multiply(num1, num2):
        sum = num1*num2
        print(num1, ' * ', num2, ' = ', sum)
    multiply(num1, num2)
