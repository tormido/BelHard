# Пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
while True:
    try:
        a = float(input("Please, input first number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
while True:
    try:
        b = float(input("Please, input second number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
while True:
    try:
        c = float(input("Please, input third number: "))
    except ValueError:
        print("it's not a number.")
    else:
        break
print(round((a + b + c)/3, 3))
